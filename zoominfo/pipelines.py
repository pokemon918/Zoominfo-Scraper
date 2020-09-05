# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter

import os


class ZoominfoPipeline:
    """Stores items in multiple CSV files according to the names of companies"""

    def open_spider(self, spider):
        self.company_name = {}

    def close_spider(self, spider):
        for exporter in self.company_name.values():
            exporter.finish_exporting()

    def _exporter_for_item(self, item):
        adapter = ItemAdapter(item)
        company = adapter['company']
        if company not in self.company_name:
            if not os.path.exists('output'):
                os.makedirs('output')
            f = open(f'output/{company}.csv', 'wb')
            exporter = CsvItemExporter(f)
            exporter.start_exporting()
            self.company_name[company] = exporter
        return self.company_name[company]

    def process_item(self, item, spider):
        exporter = self._exporter_for_item(item)
        exporter.export_item(item)
        return item

