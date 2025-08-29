# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesscraperPipeline:
    def process_item(self, item, spider):
        return item



import re

class CountriesPipeline:
    def process_item(self, item, spider):
        # Clean up the name and the continent
        if item.get('country'):
            item['country'] = item['country'].strip()
        item['continent'] = (item.get('continent') or '').strip()

        # Clean and convert population to correct number
        pop = item.get('population') or ''
        pop = re.sub(r'\[.*?\]', '', pop)
        pop = re.sub(r'[^\d]', '', pop)
        try:
            item['population'] = int(pop) if pop else None
        except Exception:
            item['population'] = None

        return item
