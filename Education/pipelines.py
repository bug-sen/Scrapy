# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EducationPipeline:
    def __init__(self):
        self.f = open("Education.xml",'wb')
    def process_item(self, items, spider):
        
        content = json.dumps(dict(items),ensure_ascii = False) + ",\n"
        self.f.write(content.encode("utf-8"))
        return items
    
    def close_url(self,spider):
        self.f.close()