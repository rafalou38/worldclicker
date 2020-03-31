from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.world)
admin.site.register(models.custom_user)