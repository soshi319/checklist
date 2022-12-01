from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Type(models.Model):
    type_text = models.CharField(max_length=50)
    def __str__(self):
        return self.type_text

class Skill(models.Model):   
    skill_text = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='skill')
    def __str__(self):
        return self.skill_text

class Point(models.Model):
    point_text = models.CharField(max_length=200)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='point')
    def __str__(self):
        return self.point_text

class Star(models.Model):
    star = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(4)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='star')
    point = models.ForeignKey(Point, on_delete=models.CASCADE, related_name='star')
    def __str__(self):
        return str(self.star)