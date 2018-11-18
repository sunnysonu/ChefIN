from rest_framework.generics import *
from app.models import *
from app.serializers.Id import *
from app.serializers.ChefProfile import *
from app.serializers.UserProfile import *
from rest_framework.permissions import IsAuthenticated

class getChefId(RetrieveAPIView):
    queryset = ChefProfile.objects.all()
    serializer_class = ChefProfileSerializer
    lookup_field = "user"
    lookup_url_kwarg = "user_id"

class getUserId(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "user"
    lookup_url_kwarg = "user_id"