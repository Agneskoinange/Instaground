from django.contrib import admin
from .models import Location,tags, Image



class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Image, ImageAdmin)