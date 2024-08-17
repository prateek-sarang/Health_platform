from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, client_register, doctor_register, client_dashboard, doctor_dashboard, send_message, send_response, user_login, csrf_failure


urlpatterns = [
    path('', home, name='home'),
    path('client_register/', client_register, name='client_register'),
    path('doctor_register/', doctor_register, name='doctor_register'),
    path('client_dashboard/', client_dashboard, name='client_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('send_message/', send_message, name='send_message'),
    path('send_response/', send_response, name='send_response'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('csrf_failure/', csrf_failure, name='csrf_failure'),
]
