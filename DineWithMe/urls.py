"""DineWithMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from users.views import signup_view, login_view, logout_view, profile_view, user_edit_view, user_delete_view
from dinners.views import feed_view, add_guest_to_dinner_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinners/', include('dinners.urls')),
    path('', login_view, name='home' ),
    path("feed/", feed_view, name='feed'),
    path('users/', include('users.urls')),
    path('logout', logout_view, name='logout'),
    path('add_guest_to_dinner/<int:my_id>/', add_guest_to_dinner_view, name = "add_guest_to_dinner"),
    path('user/<slug:my_username>/', profile_view, name="profile"),
    path('edituser/', user_edit_view, name="edit-profile"),
    path('deleteuser/', user_delete_view, name="delete-profile"),
    

    # path("signup/", signup_view, name='signup'),
    path("registrer/", signup_view, name='registrer'),    
    # path('accounts/', include('django.contrib.auth.urls'))
]
# urlpatterns += static(settings.MEDIA_URL, document_root=setings.MEDIA_ROOT)