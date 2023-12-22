# Users Setup Step 15: create a urls.py file for the users app

# users/urls.py
from django.urls import path
from .views import CreateAccountView, MyProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('my-profile/', MyProfileView.as_view(), name='myProfile'),
]