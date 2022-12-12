from django.contrib import admin
from .models import Entry, Moment, Prompt
# Register your models here.

admin.site.register(Entry)
admin.site.register(Moment)
admin.site.register(Prompt)
