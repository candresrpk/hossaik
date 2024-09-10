from django.urls import path
from .views import signupView, signinView, signoutView

app_name = 'users'

urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('signin/', signinView, name='signin'),
    path('signout/', signoutView, name='signout'),
    
]
