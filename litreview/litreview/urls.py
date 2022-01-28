"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import authentication.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('home/', review.views.home, name='home'),
    path('review/ticket_creation/', review.views.ticket_creation, name='ticket-creation'),
    path('review/view_ticket/<int:ticket_id>/', review.views.view_ticket, name='view-ticket'),
    path('review/edit_ticket/<int:ticket_id>/', review.views.edit_ticket, name='edit-ticket'),
    path('review/delete_ticket/<int:ticket_id>/', review.views.delete_ticket, name='delete-ticket'),
    path('review/review_creation/', review.views.review_creation, name='review-creation'),
    path('review/edit_review/<int:review_id>/', review.views.edit_review, name='edit-review'),
    path('posts/', review.views.posts, name='posts'),
]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
