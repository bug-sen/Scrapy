import scrapy
import json
from Education.items import EducationItem

class EducationSpider(scrapy.Spider):
    name = 'education'
   # allowed_domains = ['https://gkcx.eol.cn/school/133/']
    head_urls = "https://static-data.eol.cn/www/2.0/school/"
    button_url = "/info.json"
    #30页开始的，559页就没了
    off_set = 30
    start_urls = [head_urls + str(off_set) + button_url]
    
    def parse(self, response):
        #/span/text() intro_details_content 
        
        mode = json.loads(response.body.decode())
        
        items = EducationItem()
        items["name"] = mode["data"]["name"]
        content = mode["data"]["pro_type_min"]
        prin = content["11"]
        item = [] 
        i = 0
        js = prin[i]
        js1 = js["year"]
        ps = js["type"]["3"]
        item.append(js1)
        item.append(ps)
         
        i = i+1
        js1 = prin[i]
        js2 = js1["year"]
        ps1 = js1["type"]["1"]
        ps2 = js1["type"]["2"]
        item.append(js2)
        item.append(ps1)
        item.append(ps2)
        
        i = i+1
        js2 = prin[i]
        js3 = js2["year"]
        ps3 = js2["type"]["1"]
        ps4 = js2["type"]["2"]
        item.append(js3)
        item.append(ps3)
        item.append(ps4)
      #  for i in range(3):
       #     i = 1
        #    js = prin[i]
         #   js1 = js["year"]
            #ps = js["type"]["3"]
            
          #  i = i+1
           # item.append(js1)
            #item.append(ps)
            
        items["每年最高和最低分数线"] = item
        yield items
        
        if self.off_set<36:
            self.off_set = self.off_set+1
            url = self.head_urls + str(self.off_set) + self.button_url
            yield scrapy.Request(url,callback=self.parse)