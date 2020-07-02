from django.urls import path
from django.contrib.auth import views as auth_views

from .views.views_ import SignUpView
from .views.uta_views import SignUpUTAView, UpdateUTAView, UTAProfile


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/uta_signup/', SignUpUTAView.as_view(), name='uta_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view()),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('<pk>/uta_update_profile/', UpdateUTAView.as_view(), name='uta_update_profile' ),
    path('<pk>/', UTAProfile.as_view(), name='uta_profile'),

]
