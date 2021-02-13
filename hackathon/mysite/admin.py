from django.contrib import admin
from .models import Profile, Resource, Pin, tag

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'school', 'province')
admin.site.register (Profile, ProfileAdmin)
admin.site.register(Resource)
admin.site.register(Pin)
admin.site.register(tag)
