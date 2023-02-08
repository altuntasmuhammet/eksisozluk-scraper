from celery.decorators import task
from eksisozlukbot.eksisozlukbot.spiders.eksisozluk import EksisozlukSpider
from eksisozlukbot.eksisozlukbot import settings as eksisozlukbot_settings
from multiprocessing import Process
from scrapy import signals
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from twisted.internet import reactor

SCRAPING_HARD_TIME_LIMIT = 30


def scrape_eksisozluk(**kwargs):
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


@task(name="Scrape EksiSozluk", track_started=True, time_limit=SCRAPING_HARD_TIME_LIMIT)
def run_scrape_eksisozluk(*args, **kwargs):
    """Running eksisozluk scrapy task in celery."""
    p = Process(target=scrape_eksisozluk, args=args, kwargs=kwargs)
    p.start()
    p.join()
