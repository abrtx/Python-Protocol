
# Table of Contents

1.  [SOLID principles](#orgf4d4350)
    1.  [D (Dependency Inversion)](#orgcc91ee4)
        1.  [Python&rsquo;s Protocol](#orgb7a203f)
        2.  [Python Example](#org2b23bc1)
2.  [Libraries and utilities](#orgaf69030)
    1.  [Pydantic (Library)](#orgf633c5f)
        1.  [Why use Pydantic](#orga599785)
        2.  [How to use](#org1023758)



<a id="orgf4d4350"></a>

# SOLID principles


<a id="orgcc91ee4"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="orgb7a203f"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="org2b23bc1"></a>

### Python Example

1.  Specific class

    Examble by <https://www.youtube.com/watch?v=UvFphlHWchU&list=WL&index=6>
    
        import httpx
        import json
        
        class ScrapTopUniversity:
            ''' Web Scraping '''
        
            def __init__(self,url):
        	self.url = url
        
            def download_json(self):
        
        	self.resp = httpx.get(self.url)
        
        	for node in self.resp.json()['score_nodes']:
        	    yield node

2.  Protocol (Abstract Class)

        
        from typing import Protocol
        
        
        class WebScrap(Protocol):
            '''Protocol for Scraping classes'''
        
            def download_json(self):
        	'''Download data from web API'''

3.  How to use

    Calling Abstract class (Protocol) directly 
    instead of concrete class 
    
        from rich import print
        from libs.protocols import WebScrap
        from libs.modules import ScrapTopUniversity
        
        
        class ScrapProcessor:
        
            def download_json(self,webS: WebScrap):
        	return webS.download_json()
        
        
        def main():
        
            url = "https://www.topuniversities.com/rankings/endpoint?nid=3846212&page=4&items_per_page=15&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by=&program_type="
        
            scrap = ScrapProcessor()
            top = scrap.download_json(ScrapTopUniversity(url))
        
            for item in top:
        	print(item)
        
        
        
        if __name__ == "__main__":
            main()


<a id="orgaf69030"></a>

# Libraries and utilities


<a id="orgf633c5f"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="orga599785"></a>

### Why use Pydantic

For scrapping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="org1023758"></a>

### How to use

    from pydantic import BaseModel, validator
    
    
    class DataUni(BaseModel):
        title: str
        region: str
        stars: str
        country: str
        city: str
        rank: str
    
        @validator('stars')
        @classmethod
        def stars_default(cls, value):
    
    	if value == '':
    	    return 0

1.  main

        from rich import print
        from libs.protocols import WebScrap
        from libs.modules import ScrapTopUniversity
        from libs.models import DataUni
        
        
        class ScrapProcessor:
        
            def download_json(self, webS: WebScrap):
        	return webS.download_json()
        
        
        def main():
        
            url = "https://www.topuniversities.com/rankings/endpoint?nid=3846212&page=4&items_per_page=15&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by=&program_type="
        
            scrap = ScrapProcessor()
            top = scrap.download_json(ScrapTopUniversity(url))
        
            item = [DataUni(**t) for t in top]
        
            for row in item:
        	print(row.dict())
        
        
        if __name__ == "__main__":
            main()

