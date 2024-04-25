from django.urls import path
# from .views import UserLoginView, UserLogoutView, UserSignupView
from .views import UserLoginView, RegisterUserView,  UserLogoutView, UserVerificationEmail, SetNewPassword, PasswordResetConfirm, PasswordResetRequestView 

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('signup/', RegisterUserView.as_view(), name='user_signup'),

    path('verify-email/', UserVerificationEmail.as_view(), name='verify_email'),
    path('password-reset', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password-reset-confirm'),
    path('set-new-password', SetNewPassword.as_view(), name='set-new-password'),
]
