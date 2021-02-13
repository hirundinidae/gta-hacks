from django.contrib import admin
from .models import Profile, Resource

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'school', 'province')
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'questions', 'answers')

# Register your models here.
admin.site.register (Profile, ProfileAdmin)
admin.site.register (Resource, ResourceAdmin)
