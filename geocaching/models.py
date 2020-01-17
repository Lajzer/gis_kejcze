from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

# Create your models here.
#Package

class GeocachingUser(AbstractUser):
    favorites = models.ManyToManyField(Package)
    no_found = models.IntegerField()

class Package(models.Model):
    TYPE_CHOICES = (
        ("TRADITIONAL", "Traditional"),
        ("MULTICACHE", "Multicache"),
        ("VIRTUAL", "Virtual"),
        ("LETTERBOX", "Letterbox"),
        ("EVENT", "Event"),
        ("QUESTION", "Question"),
    )
    SIZE_CHOICES = (
        ("1", "Micro"),
        ("2", "Small"),
        ("3", "Regular"),
        ("4", "Big"),
        ("5", "Virtual"),
        ("6", "Unselected"),
        ("7", "Other"),
    )
    PACKAGE_DIFFICULTY_CHOICES = (
        ("1", "Easy"),
        ("2", "Medium-Easy"),
        ("3", "Medium"),
        ("4", "Medium-Hard"),
        ("5", "Hard"),
    )
    TERRAIN_DIFFICULTY_CHOICES = (
        ("1", "Easy"),
        ("2", "Medium-Easy"),
        ("3", "Medium"),
        ("4", "Medium-Hard"),
        ("5", "Hard"),
    )
    ATTRIBUTE_CHOICE = (
        ("1", "Dogs"),
        ("2", "Bicycle"),
        ("3", "Motorcycle"),
        ("4", "4x4"),
    )

    point = models.PointField()
    radius = models.IntegerField()
    polygon = models.PolygonField()


    name = models.CharField(max_length=60)
    description = models.TextField()
    hints = models.CharField(max_length=150)
    terrain_difficulty = models.CharField(max_length=20,
                            choices=TERRAIN_DIFFICULTY_CHOICES,
                            default="3")
    package_difficulty = models.CharField(max_length=20,
                            choices=PACKAGE_DIFFICULTY_CHOICES,
                            default="3")
    size = models.CharField(max_length=20,
                            choices=SIZE_CHOICES,
                            default="3")
    ptype = models.CharField(max_length=20,
                            choices=TYPE_CHOICES,
                            default="TRADITIONAL")
    language = models.CharField(max_length=2)
    owner = models.ForeignKeys(GeocachingUser)
    attributes = MultiSelectField(choices=ATTRIBUTE_CHOICES)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField()

    finders = models.ManyToManyField(Package)


class Comment(models.Model):
    package = models.ForeignKey(Package)
    owner = models.ForeignKeys(GeocachingUser)
    text = models.CharField(max_length=400)
    creation_date = models.DateTimeField(auto_now_add=True)

