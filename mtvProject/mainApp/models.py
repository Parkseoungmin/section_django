from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    student_ID = models.CharField(max_length=100)
    Birthday = models.DateField()
    like_food = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100)
    MTBI = models.CharField(max_length=100)
    Hobby = models.CharField(max_length=100)
    

class soccerteam(models.Model):
    Team = models.CharField(max_length=200)
    Member = models.CharField(max_length=100)
    want_meetting_day = models.DateField()
    What_you_want_to_say = models.TextField()

def summary(self):
    return self.body[:10]