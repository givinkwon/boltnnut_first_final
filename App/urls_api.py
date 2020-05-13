from django.urls import path
from .views_api import (
    SignupAPI, LoginAPI, RequestAPI, FindPasswordAPI
)

app_name = 'API'

urlpatterns = [
    path('signup/', SignupAPI, name="signup"),
    path('login/', LoginAPI, name="login"),
    path('request/', RequestAPI, name="request"),
    path('find_password/', FindPasswordAPI, name="find_password"),
]
