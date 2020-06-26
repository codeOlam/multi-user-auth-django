from django.urls import path
from django.contrib.auth import views as auth_views

from .views.signup_views import SignUpView, Profile
from .views.um1_views import SignUpUm1View, UpdateUm1View


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/um1_signup/', SignUpUm1View.as_view(), name='um1_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('<slug>/um1_update_profile/', UpdateUm1View.as_view(), name='um1_update_profile' ),
    path('<slug>/', Profile.as_view(), name='profile'),

]
