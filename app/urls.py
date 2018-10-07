from django.urls import path
from app.views.EventRequests import *
from app.views.Profile import *

app_name = "chefin"

urlpatterns = [
    path("user/", UserProfileSignup.as_view(), name="user_signup"),
    path("chef/", ChefProfileSignup.as_view(), name = "chef_signup"),
    path("", EventRequestListAPIView.as_view(), name = "EventList"),
    path("<int:pk>/", EventDetailAPIView.as_view(), name = "EventDetail"),
]