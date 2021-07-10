# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scraper.models.eksisozlukbot import Entry



class EksisozlukbotPipeline:

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        entry = Entry.objects.filter(eksisozluk_entry_id=item['eksisozluk_entry_id'])
        if entry:
            return item
            
        entry_item = Entry(**item)
        entry_item.save()

        return item
