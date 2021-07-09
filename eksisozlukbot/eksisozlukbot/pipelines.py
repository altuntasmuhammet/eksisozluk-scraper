# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from eksisozlukbot.models import Entry, create_entries_table, db_connect



class EksisozlukbotPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        engine = db_connect()
        create_entries_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        session = self.Session()
        instance = session.query(Entry).filter_by(
            eksisozluk_entry_id=item['eksisozluk_entry_id']).one_or_none()
        if instance:
            return item
            
        entry_item = Entry(**item)
        try:
            session.add(entry_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
