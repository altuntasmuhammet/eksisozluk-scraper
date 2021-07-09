import scrapy

import time
from datetime import datetime
import urllib.parse

EKSISOZLUK_BASEURL = "https://eksisozluk.com"
DATETIME_FORMAT = "%d.%m.%Y %H:%M"
start_date = ""
end_date = ""
keywords = ["apache kafka"]

class EksisozlukSpider(scrapy.Spider):
    name = 'eksisozluk'
    allowed_domains = ['eksisozluk.com']
    # start_urls = ['http://eksisozluk.com/']

    def start_requests(self):
        title_query_url_templated = "https://eksisozluk.com/basliklar/ara?SearchForm.Keywords={keyword}&SearchForm.Author=&SearchForm.When.From={start_date}&SearchForm.When.To={end_date}&SearchForm.NiceOnly=false&SearchForm.FavoritedOnly=false&SearchForm.SortOrder=Date&_={timestamp}"
        for keyword in keywords:
            encoded_keyword = urllib.parse.quote(keyword) 
            timestamp = int(time.time() * 1000)
            url = title_query_url_templated.format(keyword=encoded_keyword,
                                                   start_date=start_date,
                                                   end_date=end_date,
                                                   timestamp=timestamp)
            print("******URL****** - {}".format(url))
            yield scrapy.Request(url=url, callback=self.parse_title_links)

    def parse_title_links(self, response):
        print()
        titles = response.css('div.instapaper_body ul.topic-list li')
        print("********TITLE********:", titles)
        for title in titles:
            title_url = EKSISOZLUK_BASEURL + title.css('a::attr(href)').get()
            title_name = title.css("a::text").get().strip()
            yield scrapy.Request(url=title_url, callback=self.parse_pages, meta={'title_url': title_url, 'title_name': title_name})
    
    def parse_pages(self, response):
        page_count_str = response.css('div.pager::attr(data-pagecount)').get()
        page_count = int(page_count_str) if page_count_str else 1
        title_url = response.meta['title_url']
        title_name = response.meta['title_name']
        for page_num in range(1, page_count+1):
            url = "{title_url}?p={page_num}".format(title_url=title_url, page_num=page_num)
            yield scrapy.Request(url=url, callback=self.parse_entries_per_page, meta={'title_name':title_name})
    
    def parse_entries_per_page(self, response):
        entries = response.css('ul[id=entry-item-list] li')
        title_name = response.meta['title_name']
        for entry in entries:
            # Content
            content = " ".join(entry.css("div.content *::text").getall()).strip()
            print("******LOG****** - Content:", content)
            # Title
            title = title_name
            # Favourite Count
            favourite_count = int(entry.attrib['data-favorite-count'])
            # Author Name
            author = entry.css("footer div.info a.entry-author::text").get().strip()
            # Created Date and Edited Date
            date = entry.css("footer div.info a.entry-date::text").get().strip()
            if '~' in date:
                created_date_str = date.split('~')[0].strip()
                edited_date_str = date.split('~')[1].strip()
                print("LOG 1", created_date_str, edited_date_str)
                edited_date_str = edited_date_str if len(edited_date_str)==len(created_date_str) else " ".join([created_date_str.split(' ')[0], edited_date_str])
                print("LOG 2", created_date_str, edited_date_str)
                created_date = datetime.strptime(created_date_str, DATETIME_FORMAT)
                edited_date = datetime.strptime(edited_date_str, DATETIME_FORMAT)
            else:
                created_date_str = date.strip()
                created_date = datetime.strptime(created_date_str, DATETIME_FORMAT)
                edited_date = None
            # eksisozluk_entry_id
            eksisozluk_entry_id = int(entry.attrib['data-id'])
            # eksisozluk_author_id
            eksisozluk_author_id = int(entry.attrib['data-author-id'])
            yield {
                "content": content,
                "title": title,
                "favourite_count": favourite_count,
                "author": author,
                "created_date": created_date,
                "edited_date": edited_date,
                "eksisozluk_entry_id": eksisozluk_entry_id,
                "eksisozluk_author_id": eksisozluk_author_id
            }