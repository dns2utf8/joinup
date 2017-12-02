from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Tag)
admin.site.register(models.Group)
admin.site.register(models.Event)
admin.site.register(models.Comment)