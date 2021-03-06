from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.
class tag(models.Model):
    name=models.CharField(max_length=200)
    def __str__ (self):
        return self.name
class Resource(models.Model):
    name = models.CharField(max_length=50)
    questions = models.CharField(max_length=300)
    answers = models.CharField(max_length=300, blank=True)
    tag_list=models.ManyToManyField('tag')

    def get_absolute_url(self):
        return f'{self.id}'
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=50)
    prov_choices = [
        ('QC', 'Quebec'),
        ('BC', 'British Columbia'),
        ('ON', 'Ontario'),
        ('AL', 'Alberta'),
        ('MB', 'Manitoba'),
        ('SK', 'Saskatchewan'),
        ('NL', 'Newfoundland and Labrador'),
        ('PE', 'Prince Edward Island'),
        ('NS', 'Nova Scotia'),
        ('NB', 'New Brunswick'),
    ]
    prov_choices.sort()
    province = models.CharField(max_length=50, choices=prov_choices)
    def get_absolute_url(self):
        return f'{self.id}'
class Pin(models.Model):
    prof = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.ForeignKey(Resource, on_delete=models.CASCADE)

class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=20)
    bio = models.CharField(max_length=200, blank=True)
    school = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, blank=True)
    prov_choices = [
        ('QC', 'Quebec'),
        ('BC', 'British Columbia'),
        ('ON', 'Ontario'),
        ('AL', 'Alberta'),
        ('MB', 'Manitoba'),
        ('SK', 'Saskatchewan'),
        ('NL', 'Newfoundland and Labrador'),
        ('PE', 'Prince Edward Island'),
        ('NS', 'Nova Scotia'),
        ('NB', 'New Brunswick'),
    ]
    prov_choices.sort()
    province = models.CharField(max_length=50, choices=prov_choices)
    USERNAME_FIELD = 'username'
