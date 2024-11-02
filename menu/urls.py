from django.urls import path,include
from . import views 
from .views import signup

urlpatterns = [
    path('', views.view_menu, name='menu'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('sugg/', views.sugg_view, name='sugg'),
    path('signup/', signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    # path('accounts/', include('allauth.urls')),  # Include Allauth URLs

]