from django.db import models

from main.models import User


class Team(models.Model):
    team_name = models.CharField(max_length=100, unique=True)
    team_desc = models.TextField(blank=True, default='')
    creation_date = models.DateField(auto_now_add=True)
    captain_id = models.IntegerField(blank=True, null=False, unique=True)
    place = models.IntegerField(default=0, blank=True)
    points = models.FloatField(default=0.0, blank=True)
    is_available = models.BooleanField(default=True)
    played_games = models.IntegerField(default=0, blank=True)
    team_members = models.ManyToManyField(User, related_name="teams", through="UserTeam")

    def get_captain_name(self):
        user = User.objects.get(pk=self.captain_id)
        return user.username


class UserTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
