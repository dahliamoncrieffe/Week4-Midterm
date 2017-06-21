from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Media(models.Model):
    media_type = models.CharField(max_length=128)
    title = models.CharField(max_length=100)
    isbn = models.IntegerField(unique=True)
    author = models.CharField(max_length=150)
    image = models.ImageField

    slug = models.SlugField(blank=True, default='')

    def save(self, *args, **kwargs):
        self.slug =slugify(self.title)
        super(Media,self).save(*args, **kwargs)

    def __str__(self): #For Python 2, use __unicode__ too
        return self.title + " by " + self.author


class Topic(models.Model):
    topic = models.CharField(max_length=75)

    def __str__(self): #For Python 2, use _unicode__ too
        return self.topic

class User(models.Model):
    user_id = models.CharField(max_length=15, unique=True, null=False)
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.user_id
