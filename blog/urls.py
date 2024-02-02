from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('user_login', views.user_login, name='user_login'),
    path('Bimar_dashboard/', views.Bimar_dashboard, name='Bimar_dashboard'),
    path('Monshi_dashboard/', views.Monshi_dashboard, name='Monshi_dashboard'),
    path('add_clinic/', views.add_clinic, name='add_clinic'),
    
    path('signup.html/', views.signup , name='signup.html'),
    path('login/signup.html/login.html', views.login, name= 'login.html')
    
]
