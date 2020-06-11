from django.contrib import admin

from .models import Photo
from .models import Diagnosis

admin.site.register(Photo)
admin.site.register(Diagnosis)
