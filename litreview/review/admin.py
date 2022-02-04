from django.contrib import admin

from review.models import ticket, review, userfollows


class TicketAdmin(admin.ModelAdmin):
    """For administration panel"""
    list_display = ('title', 'description', 'image', 'user', 'is_archived')

class ReviewAdmin(admin.ModelAdmin):
    """For administration panel"""
    list_display = ('ticket', 'headline', 'rating', 'user','get_is_archived')

    def get_is_archived(self, obj):
        return obj.ticket.is_archived

    get_is_archived.short_description = 'is_archived'
    get_is_archived.admin_order_field = 'is_archived'

class UserFollowsAdmin(admin.ModelAdmin):
    """For administration panel"""
    list_display = ['user', 'followed_user']

admin.site.register(ticket.Ticket, TicketAdmin)
admin.site.register(review.Review, ReviewAdmin)
admin.site.register(userfollows.UserFollows, UserFollowsAdmin)
