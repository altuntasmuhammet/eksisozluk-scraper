from celery.decorators import task
from eksisozlukbot.eksisozlukbot.spiders.eksisozluk import EksisozlukSpider
from eksisozlukbot.eksisozlukbot import settings as eksisozlukbot_settings
from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os


@task(name="Scrape EksiSozluk", track_started=True)
def scrape_eksisozluk(**kwargs):
    # process = CrawlerProcess(settings=get_project_settings())
    # process.crawl(EksisozlukSpider)
    # process.start()
    crawler_settings = Settings()
    crawler_settings.setmodule(eksisozlukbot_settings)

    #Create a crawler
    crawler = Crawler(EksisozlukSpider, settings=crawler_settings)

    # This ensures Twisted Reactor is properly shutdown
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)

    # Start crawling
    crawler.crawl(**kwargs)

    # add blocking process
    reactor.run()