from rest_framework.generics import *
from app.models import *
from app.serializers.EventRequests import *
from rest_framework.permissions import IsAuthenticated

class EventRequestListAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if(self.request.method == "GET"):
            return EventRequestsListSerializer
        elif(self.request.method == "POST"):
            return EventRequestsDetailSerializer

    def get_queryset(self):
        return EventRequests.objects.all()

class EventDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EventRequestsDetailSerializer
    queryset = EventRequests.objects.all()