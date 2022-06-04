from django.contrib import admin
# add model to admin
from .models import Snack

# Register your models here.
admin.site.register(Snack)