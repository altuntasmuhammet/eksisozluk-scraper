from django.contrib import admin
from .models import Entry

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "favourite_count", "author", "created_date", "edited_date")

admin.site.register(Entry, EntryAdmin)