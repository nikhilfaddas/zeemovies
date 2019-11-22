from django.db import models

# Create your models here.
class User(models.Model):
    uName = models.CharField(max_length=50)
    uAge = models.IntegerField()
    uGender = models.CharField(max_length=80)


class Movies(models.Model):
    mName = models.CharField(max_length=50)
    mRdate = models.DateField()
    mLang = models.CharField(max_length=80)
    # actmovie = models.ManyToManyField(Actor)