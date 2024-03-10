
# Table of Contents

1.  [Python&rsquo;s Features](#org08d27c6)
2.  [SOLID principles](#org02b4f06)
    1.  [D (Dependency Inversion)](#org6e8b0b9)
        1.  [Python&rsquo;s Protocol](#orgcfac4a4)
        2.  [Python Example](#org8754192)
3.  [Libraries and utilities](#org15373ef)
    1.  [Pydantic (Library)](#org85c6fb8)
        1.  [Why use Pydantic](#org614fd4c)
        2.  [How to use](#org448f0c5)



<a id="org08d27c6"></a>

# Python&rsquo;s Features

In data projects we need to solve issues. Abstract methods, 
data modelers and data validators come to help there.
That&rsquo;s what I try to show here


<a id="org02b4f06"></a>

# SOLID principles


<a id="org6e8b0b9"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="orgcfac4a4"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="org8754192"></a>

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


<a id="org15373ef"></a>

# Libraries and utilities


<a id="org85c6fb8"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="org614fd4c"></a>

### Why use Pydantic

For scrapping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="org448f0c5"></a>

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

