from django.contrib import admin
from .models import Temperature, Config

# Register your models here.
admin.site.register(Temperature)
admin.site.register(Config)