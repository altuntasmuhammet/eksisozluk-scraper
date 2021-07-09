from celery.decorators import task
from eksisozlukbot.eksisozlukbot.spiders.eksisozluk import EksisozlukSpider
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess


@task(name="Scrape EksiSozluk", track_started=True)
def scrape_eksisozluk():
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(EksisozlukSpider)
    process.start()