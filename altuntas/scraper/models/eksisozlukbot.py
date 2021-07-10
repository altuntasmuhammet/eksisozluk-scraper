from django.conf import settings
from django.db import models


class Entry(models.Model):
    title = models.TextField()
    content = models.TextField()
    favourite_count = models.IntegerField()
    author = models.TextField()
    created_date = models.DateTimeField()
    edited_date = models.DateTimeField(blank=True)
    eksisozluk_entry_id = models.IntegerField(unique=True)
    eksisozluk_author_id = models.IntegerField()

    class Meta:
        app_label = "scraper"
        db_table = "scraper_eksisozluk_entries"
        verbose_name_plural = "Eksisozluk Entries"
        verbose_name = "Eksisozluk Entry"
        # abstract=True
