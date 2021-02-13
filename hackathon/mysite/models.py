from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class tag(models.Model):
    name=models.CharField(max_length=200)
class Resource(models.Model):
    name = models.CharField(max_length=50)
    questions = models.FileField()
    answers = models.FileField(blank=True)
    tag_list=models.ManyToManyField('tag')
    description=models.CharField(max_length=2000, blank=True)

    def clean(self, *args, **kwargs):
        Qdoc = self.questions
        Qname = Qdoc.name
        if not Qname.endswith('.pdf'):
            raise ValidationError('File type not supported')
        if self.answers is None:
            print('NONE')
        else:
            print('NOT NONE')
            Adoc = self.answers
            Aname = Adoc.name
            if not Aname.endswith('.pdf') and Aname is not '':
                print('ERROR')
                raise ValidationError('File type not supported')

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
    province = models.CharField(max_length=50, choices=prov_choices)

class Pin(models.Model):
    prof = models.ForeignKey('Profile', on_delete=models.CASCADE)
    file = models.ForeignKey('Resource', on_delete=models.CASCADE)
