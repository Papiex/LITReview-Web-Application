from django.contrib import admin

from review.models import Ticket, Review


class TicketAdmin(admin.ModelAdmin):
    """For administration panel"""
    list_display = ('title', 'description', 'image', 'user')

class ReviewAdmin(admin.ModelAdmin):
    """For administration panel"""
    list_display = ('headline', 'rating', 'ticket', 'user')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Review, ReviewAdmin)
