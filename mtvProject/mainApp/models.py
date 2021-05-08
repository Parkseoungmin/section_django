from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()

class soccerteam(models.Model):
    Team = models.CharField(max_length=200)
    Member = models.CharField(max_length=100)
    want_meetting_day = models.DateField()
    What_you_want_to_say = models.TextField()
