from django.urls import path
from app.views.EventRequests import *
from app.views.Profile import *

app_name = "chefin"

urlpatterns = [
    path("user/", UserProfileSignup.as_view(), name="user_signup"),
    path("chef/", ChefProfileSignup.as_view(), name = "chef_signup"),
    path("user/<int:pk>/", UserDetailProfile.as_view(), name = "user"),
    path("chef/<int:pk>/", ChefDetailProfile.as_view(), name = "chef"),
    path("", EventRequestListAPIView.as_view(), name = "EventList"),
    path("<int:pk>/", EventDetailAPIView.as_view(), name = "EventDetail"),
]