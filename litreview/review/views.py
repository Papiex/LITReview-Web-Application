from itertools import chain

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import CharField, Value

from .models.ticket import Ticket
from .models.review import Review
from .models.userfollows import UserFollows
from .forms.ticket_form import TicketForm
from .forms.review_form import ReviewForm


@login_required
def home(request):
    """
    Redirect to home.html
    """
    return render(request, 'review/home.html')

@login_required
def posts(request):
    """
    Get list of all tickets and reviews and redirect to posts.html
    """
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)

    return render(request, 'review/posts.html', context={'posts': posts})

@login_required
def ticket_creation(request):
    """get the ticket form and create ticket"""
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('home')
    return render(request, 'review/ticket_creation.html', context={'form': form})

@login_required
def edit_ticket(request, ticket_id: int):
    """
    Get info of selected ticket for editing and saving
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    edit_form = TicketForm(instance=ticket)
    if request.method == 'POST':
        edit_form = TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('posts')
    return render(request, 'review/edit_ticket.html', context={'edit_form': edit_form, 'ticket': ticket})

@login_required
def delete_ticket(request, ticket_id: int):
    """
    Get instance of selected ticket and set 'is_archived' to True
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.is_archived = True
        ticket.save(update_fields=['is_archived'])
        return redirect('posts')
    return render(request, 'review/delete_ticket.html', {'ticket': ticket})

@login_required
def review_creation(request):
    """create review"""
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.is_processed = True
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {'ticket_form': ticket_form, 'review_form': review_form}
    return render(request, 'review/review_creation.html', context=context)

@login_required
def review_response_ticket(request, ticket_id: int):
    """
    Get the chosen ticket instance for adding a review
    and set true for hiding the option "ajouter une critique".
    """
    ticket = get_object_or_404(Ticket, id=ticket_id)
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            ticket.is_processed = True
            ticket.save(update_fields=['is_processed'])
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {'review_form': review_form, 'ticket': ticket}
    return render(request, 'review/review_creation_ticket.html', context=context)

@login_required
def edit_review(request, review_id: int):
    """get info of reviews for editing and saving"""
    review = get_object_or_404(Review, id=review_id)
    edit_form = ReviewForm(instance=review)
    if request.method == 'POST':
        edit_form = ReviewForm(request.POST, request.FILES, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('posts')
    return render(request, 'review/edit_review.html', context={'edit_form': edit_form})

@login_required
def delete_review(request, review_id: int):
    """Get and delete the selected review"""
    review = get_object_or_404(Review, id=review_id)
    ticket = get_object_or_404(Ticket, id=review.ticket.id)
    ticket.is_processed = False
    ticket.save(update_fields=['is_processed'])
    if request.method == 'POST':
        review.delete()
        return redirect('posts')
    return render(request, 'review/delete_review.html', {'review': review})

@login_required
def flux(request):
    """flux"""
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    User = get_user_model()
    users = User.objects.all()

    followeds = UserFollows.objects.filter(user=request.user).select_related("followed_user")
    followeds_group = [user.followed_user for user in followeds]
    followeds_group.append(request.user)
    print(followeds_group)

    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True
    )

    return render(request, 'review/flux.html', context={'posts': posts, 'users': users, 'followeds': followeds_group})

@login_required
def subscription_view(request):
    """
    Display the followed users and the followers users
    also search function with suggestion of existing users
    """
    User = get_user_model()
    users = User.objects.all()
    subscriptions = UserFollows.objects.filter(user=request.user)
    subscribers = UserFollows.objects.filter(followed_user=request.user)
    context = {'users': users, 'subscribers': subscribers, 'subscriptions': subscriptions}
    if request.method == 'POST':
        username_search = request.POST.get('research')
        search = User.objects.filter(username=username_search)

        already_subscribe = False
        for user in subscriptions:
            if user.followed_user.username == username_search:
                already_subscribe = True

        context['search'] = search
        context['already_subscribe'] = already_subscribe
        return render(request, 'review/subscription.html', context=context)
    return render(request, 'review/subscription.html', context=context)

@login_required
def subscribing(request, adding_follower_id=False, deleting_follower_id=False):
    """
    Add or deleting subscriber
    'adding_follower_id' and 'deleting_follower_id' will be replaced by the chosen user id
    """
    User = get_user_model()
    users = User.objects.all()
    if adding_follower_id:
        subscribe_to_user = users.get(id=adding_follower_id)
        followed = UserFollows(user=request.user, followed_user=subscribe_to_user)
        followed.save()
        return redirect('subscription')
    if deleting_follower_id:
        get_subscribing_user = users.get(id=deleting_follower_id)
        delete_subscribe = UserFollows.objects.get(user=request.user, followed_user=get_subscribing_user)
        delete_subscribe.delete()
        return redirect('subscription')