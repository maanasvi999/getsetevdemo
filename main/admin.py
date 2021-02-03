from django.contrib import admin
from .models import EVCategory, EVInformation, ModelsInfo, EVHighlights, EVColorCustom, Subscribers
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
admin.site.register(EVCategory)
admin.site.register(EVInformation)
admin.site.register(ModelsInfo)
admin.site.register(EVHighlights)
admin.site.register(EVColorCustom)
admin.site.register(Subscribers)