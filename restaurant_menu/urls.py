
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',include('menu.urls')),
    # path('test/',include('menu.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('sugg/',include('menu.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('signup/',include('menu.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include default Django auth URLs
    

]
