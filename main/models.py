from django.db import models
from django.contrib.auth.models import User


class WorkStream(models.Model):
    short_name = models.CharField(max_length=6, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    budget_link = models.URLField(max_length=400)
    current_gtc_num = models.URLField(max_length=400)
    current_gtc_graph = models.URLField(max_length=400)
    current_stable_num = models.URLField(max_length=400)
    current_stable_graph = models.URLField(max_length=400)
    all_time_contributors = models.URLField(max_length=400)

    def __str__(self):
        return self.short_name

    # TODO: Add field in serializer for leads using a method field


class Steward(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workstream = models.ForeignKey(WorkStream, on_delete=models.CASCADE)
    steward_since = models.DateTimeField(auto_now=True)
    statement_post = models.URLField(max_length=400)
    gitcoin_username = models.CharField(max_length=60, unique=True)
    discourse_username = models.CharField(max_length=60, unique=True)
    profile_image = models.URLField(
        null=True, blank=True,
        max_length=400)  # maybe replace with a proper upload later

    def __str__(self):
        return f'{self.name} : {self.workstream.short_name}'
