from django.contrib import admin
from .models import Profile, Resource, tag, MyUser

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'school', 'province')
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'questions', 'answers')
class tagAdmin(admin.ModelAdmin):
    pass
class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'bio', 'school', 'province')
# Register your models here.
admin.site.register (Profile, ProfileAdmin)
admin.site.register(tag, tagAdmin)
admin.site.register (Resource, ResourceAdmin)
admin.site.register (MyUser, MyUserAdmin)
