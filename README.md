
# Table of Contents

1.  [Python&rsquo;s Features](#orgad78422)
2.  [SOLID principles](#orgeb6853a)
    1.  [D (Dependency Inversion)](#org98b57a7)
        1.  [Python&rsquo;s Protocol](#org113b38d)
        2.  [Python Example](#org9f498c4)
3.  [Libraries and utilities](#org4772935)
    1.  [Pydantic (Library)](#org850979f)
        1.  [Why use Pydantic](#orgb928ca5)
        2.  [How to use](#org36c3f25)
    2.  [Dependency Injection (programming technique)](#org7c452de)
        1.  [Why use Dependency Injection](#orgdac62d5)
        2.  [How to use](#org461017b)
    3.  [PySpark](#org57aa3d0)
        1.  [How to use](#org0718459)



<a id="orgad78422"></a>

# Python&rsquo;s Features

In data projects we need to solve issues. Abstract methods, 
data modelers and data validators come to help there.
That&rsquo;s what I try to show here.


<a id="orgeb6853a"></a>

# SOLID principles


<a id="org98b57a7"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="org113b38d"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="org9f498c4"></a>

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


<a id="org4772935"></a>

# Libraries and utilities


<a id="org850979f"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="orgb928ca5"></a>

### Why use Pydantic

For scraping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="org36c3f25"></a>

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


<a id="org7c452de"></a>

## Dependency Injection (programming technique)

An object or function receives other objects or 
functions instead of creating it.


<a id="orgdac62d5"></a>

### Why use Dependency Injection

Because it helps to decrease coupling and increase 
cohesion. Those metrics are often inversely correlated.
We need to procure low coupling and high cohesion. 


<a id="org461017b"></a>

### How to use

In the previous example we can see it was applied.
Here we can see that download<sub>json</sub> function receive
WebScrap instead of create it.

    from libs.protocols import WebScrap
    
    
    class ScrapProcessor:
    
        def download_json(self,webS: WebScrap):
    	return webS.download_json()


<a id="org57aa3d0"></a>

## PySpark

PySpark is the Python API for Apache Spark. 
It enables you to perform real-time, large-scale 
data processing in a distributed environment using Python.
For more information: <https://spark.apache.org/docs/latest/api/python/index.html#:~:text=PySpark%20is%20the%20Python%20API,for%20interactively%20analyzing%20your%20data>.


<a id="org0718459"></a>

### How to use

1.  Config

        from pyspark.sql import SparkSession
        from pyspark import SparkConf
        
        
        conf = SparkConf().setAppName("MyScraper") \
        	    .setMaster("local[2]") \
        	    .set("spark.executor.memory", "2g") \
        	    .set("spark.executor.cores", "2")
        
        sc = SparkSession.builder.config(conf=conf).getOrCreate()
        
        print(SparkConf().getAll())

2.  Using with Scraper

        
        def main():
        
            url = "https://www.topuniversities.com/rankings/endpoint?nid=3846212&page=4&items_per_page=15&tab=&region=&countries=&cities=&search=&star=&sort_by=&order_by=&program_type="
        
            scrap = ScrapProcessor()
            top = scrap.download_json(ScrapTopUniversity(url))
        
            item = [DataUni(**t) for t in top]
        
            # for row in item:
            #     print(row.dict())
        
            df = sc.createDataFrame(data=item) # create into Spark context
        
            df.show(truncate=False)
        
            df.createOrReplaceTempView("table") # using like SQL language
            sc.sql('select title, rank from table order by rank desc').show(20, False)

