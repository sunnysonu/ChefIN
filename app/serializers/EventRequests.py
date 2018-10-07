from rest_framework import serializers
from app.models import EventRequests

class EventRequestsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRequests
        fields = ("event_name", "location", "people", "dishes", "request_by", "accepted_by", )

class EventRequestsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventRequests
        fields = ("event_name", "location", "people", "dishes", "request_by", "accepted_by", )
# depth = 1 wont accept foreign keys
