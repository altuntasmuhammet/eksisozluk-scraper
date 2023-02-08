from rest_framework import serializers

from scraper.models import Entry
from scraper.models.eksisozlukbot import Entry


class EksiSozlukEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "title", "content", "favourite_count", "author",
                  "created_date", "edited_date", "eksisozluk_entry_id", "eksisozluk_author_id"]
