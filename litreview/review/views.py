from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import forms
from . import models


@login_required
def home(request):
    """redirect to home.html"""
    return render(request, 'review/home.html')

@login_required
def posts(request):
    """redirect to posts.html"""
    tickets = models.Ticket.objects.all()
    reviews = models.Review.objects.all()
    return render(request, 'review/posts.html', context={'tickets': tickets, 'reviews': reviews})

@login_required
def ticket_creation(request):
    """get the ticket form and create ticket"""
    form = forms.TicketForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('home')
    return render(request, 'review/ticket_creation.html', context={'form': form})

@login_required
def view_ticket(request, ticket_id: int):
    """view info of ticket"""
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'review/view_ticket.html', {'ticket': ticket})

@login_required
def edit_ticket(request, ticket_id: int):
    """get info of ticket and edit it"""
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    if request.method == 'POST':
        edit_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('posts')
    return render(request, 'review/edit_ticket.html', context={'edit_form': edit_form})

@login_required
def delete_ticket(request, ticket_id):
    """delete ticket"""
    ticket = models.Ticket.objects.filter(id=ticket_id)
    ticket.delete()
    return redirect('posts')

@login_required
def review_creation(request):
    """create review"""
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {'ticket_form': ticket_form, 'review_form': review_form}
    return render(request, 'review/review_creation.html', context=context)

@login_required
def edit_review(request, review_id: int):
    """get info of review and edit it"""
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    if request.method == 'POST':
        edit_form = forms.ReviewForm(request.POST, request.FILES, instance=review)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('posts')
    return render(request, 'review/edit_review.html', context={'edit_form': edit_form})