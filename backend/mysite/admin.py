from django.contrib import admin
from .models import Profile, Resource, tag

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'school', 'province')
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'questions', 'answers')
class tagAdmin(admin.ModelAdmin):
    pass
# Register your models here.
admin.site.register (Profile, ProfileAdmin)
admin.site.register(tag, tagAdmin)
admin.site.register (Resource, ResourceAdmin)
