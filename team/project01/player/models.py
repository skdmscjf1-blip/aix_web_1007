from django.db import models
from team.models import Team

class Player(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    position = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.team},{self.name},{self.number},{self.position},{self.age}'