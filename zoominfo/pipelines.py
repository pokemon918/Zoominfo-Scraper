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
        if not os.path.exists('output'):
            os.makedirs('output')

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        f = open(f'output/{adapter["company"]}.csv', 'wb')
        exporter = CsvItemExporter(f, fields_to_export=['headquarters', 'phone', 'revenue', 'employees_num', 'website'])
        exporter.start_exporting()
        exporter.export_item(item)
        exporter.finish_exporting()
        return item

