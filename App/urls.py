from django.urls import path
from .views import (
    MainPage, LoginPage, LogoutPage, SignupPage, SignupSuccessPage, PartnerPage, PartnerDetailPage, ProjectPage, ProjectDetailPage,
    ConsultingPage, RequestPage, ProductPage, PersonalPage, TermsPage
)

app_name = 'Page'

urlpatterns = [
    path('', MainPage, name="main"),
    path('login/', LoginPage, name="login"),
    path('logout/', LogoutPage, name="logout"),

    path('signup/', SignupPage, name="signup"),
    path('signup/success', SignupSuccessPage, name="signup-success"),

    path('partner/', PartnerPage, name="partner"),
    path('partner/<str:id>/', PartnerDetailPage, name="partner-detail"),
    path('project/', ProjectPage, name="project"),
    path('project/<str:id>/', ProjectDetailPage, name="project-detail"),

    path('consulting/', ConsultingPage, name="consulting"),
    path('product/', ProductPage, name="product"),
    path('request/', RequestPage, name="request"),
    path('personal/', PersonalPage, name="personal"),
    path('terms/', TermsPage, name="terms"),
]
