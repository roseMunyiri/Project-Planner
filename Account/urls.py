from django.urls import path
from .views import UserLoginView, UserLogoutView, UserSignupView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('signup/', UserSignupView.as_view(), name='user_signup'),
]
