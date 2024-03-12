
# Table of Contents

1.  [Python&rsquo;s Features](#org4ab680f)
2.  [SOLID principles](#orgecc9a42)
    1.  [D (Dependency Inversion)](#org573a229)
        1.  [Python&rsquo;s Protocol](#orgc5c71d2)
        2.  [Python Example](#orge953bc1)
3.  [Libraries and utilities](#org609ca68)
    1.  [Pydantic (Library)](#org04a6a23)
        1.  [Why use Pydantic](#orgf7552d7)
        2.  [How to use](#org8754e26)
    2.  [Dependency Injection (programming technique)](#org04945df)
        1.  [Why use Dependency Injection](#org0bc3bc7)
        2.  [How to use](#orgb2c627d)



<a id="org4ab680f"></a>

# Python&rsquo;s Features

In data projects we need to solve issues. Abstract methods, 
data modelers and data validators come to help there.
That&rsquo;s what I try to show here.


<a id="orgecc9a42"></a>

# SOLID principles


<a id="org573a229"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="orgc5c71d2"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="orge953bc1"></a>

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


<a id="org609ca68"></a>

# Libraries and utilities


<a id="org04a6a23"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="orgf7552d7"></a>

### Why use Pydantic

For scraping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="org8754e26"></a>

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


<a id="org04945df"></a>

## Dependency Injection (programming technique)

An object or function receives other objects or 
functions instead of creating it.


<a id="org0bc3bc7"></a>

### Why use Dependency Injection

Because it helps to decrease coupling and increase 
cohesion. Those metrics are often inversely correlated.
We need to procure low coupling and high cohesion. 


<a id="orgb2c627d"></a>

### How to use

In the previous example we can see it was applied.
Here we can see that download<sub>json</sub> function receive
WebScrap instead of create it.

    from libs.protocols import WebScrap
    from libs.modules import ScrapTopUniversity
    
    
    class ScrapProcessor:
    
        def download_json(self,webS: WebScrap):
    	return webS.download_json()

