from djongo import models
from bson import ObjectId

class ObjectIdField(models.Field):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 24
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        if not value:
            return ObjectId()
        if not isinstance(value, ObjectId):
            return ObjectId(value)
        return value

class User(models.Model):
    id = ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)

class Team(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    id = ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = ObjectIdField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    id = ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()