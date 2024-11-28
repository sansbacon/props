from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Redirect the root path to the login page
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('accounts/', include('allauth.urls')),  # Allauth URLs for login/logout
    path('', lambda request: redirect('account_login')),  # Redirect root to login
]
