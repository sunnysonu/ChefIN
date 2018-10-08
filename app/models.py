from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)

    class Meta:
        unique_together = ("username", )

class ChefProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    dishes = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length = ((10 + 1) * 100)
    )

    class Meta:
        unique_together = ("username", )

class EventRequests(models.Model):
    request_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    accepted_by = models.ForeignKey(ChefProfile, on_delete=models.CASCADE, blank = True, null=True)
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    people = models.IntegerField()
    dishes = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length = ((10 + 1) * 100)
    )
    time = models.DateTimeField(auto_now_add=True)