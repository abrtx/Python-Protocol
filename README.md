
# Table of Contents

1.  [Python&rsquo;s Features](#orgc95a6d2)
2.  [SOLID principles](#orgbeea2cd)
    1.  [D (Dependency Inversion)](#org3faa540)
        1.  [Python&rsquo;s Protocol](#org354e812)
        2.  [Python Example](#org1775fec)
3.  [Libraries and utilities](#orgf54bd78)
    1.  [Pydantic (Library)](#org5cd20b6)
        1.  [Why use Pydantic](#orgae2d2b6)
        2.  [How to use](#org0896508)
    2.  [Dependency Injection (programming technique)](#org7eca403)
        1.  [Why use Dependency Injection](#orgc39a602)
        2.  [How to use](#org4f7f043)
    3.  [PySpark](#orgb33bfc5)
        1.  [How to use](#org66258c7)



<a id="orgc95a6d2"></a>

# Python&rsquo;s Features

In data projects we need to solve issues. Abstract methods, 
data modelers and data validators come to help there.
That&rsquo;s what I try to show here.


<a id="orgbeea2cd"></a>

# SOLID principles


<a id="org3faa540"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="org354e812"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="org1775fec"></a>

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


<a id="orgf54bd78"></a>

# Libraries and utilities


<a id="org5cd20b6"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="orgae2d2b6"></a>

### Why use Pydantic

For scraping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="org0896508"></a>

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


<a id="org7eca403"></a>

## Dependency Injection (programming technique)

An object or function receives other objects or 
functions instead of creating it.


<a id="orgc39a602"></a>

### Why use Dependency Injection

Because it helps to decrease coupling and increase 
cohesion. Those metrics are often inversely correlated.
We need to procure low coupling and high cohesion. 


<a id="org4f7f043"></a>

### How to use

In the previous example we can see it was applied.
Here we can see that download<sub>json</sub> function receive
WebScrap instead of create it.

    from libs.protocols import WebScrap
    
    
    class ScrapProcessor:
    
        def download_json(self,webS: WebScrap):
    	return webS.download_json()


<a id="orgb33bfc5"></a>

## PySpark

PySpark is the Python API for Apache Spark. 
It enables you to perform real-time, large-scale 
data processing in a distributed environment using Python.
For more information: <https://spark.apache.org/docs/latest/api/python/index.html#:~:text=PySpark%20is%20the%20Python%20API,for%20interactively%20analyzing%20your%20data>.


<a id="org66258c7"></a>

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
    
    1.  Example
    
            +---------------+----------------+----+-------------+-----+----------------------------------------------------------+
            |city           |country         |rank|region       |stars|title                                                     |
            +---------------+----------------+----+-------------+-----+----------------------------------------------------------+
            |Mexico City    |Mexico          |61  |Latin America|0    |Universidad Nacional Autónoma de México  (UNAM)           |
            |Seattle        |United States   |62  |North America|0    |University of Washington                                  |
            |Dhahran        |Saudi Arabia    |63  |Asia         |0    |King Fahd University of Petroleum & Minerals              |
            |Paris          |France          |64  |Europe       |0    |Sorbonne University                                       |
            |Barcelona      |Spain           |65  |Europe       |0    |Universitat Politècnica de Catalunya · BarcelonaTech (UPC)|
            |Kuala Lumpur   |Malaysia        |66  |Asia         |0    |Universiti Malaya (UM)                                    |
            |Kyoto          |Japan           |67  |Asia         |0    |Kyoto University                                          |
            |Chennai        |India           |68  |Asia         |0    |Indian Institute of Technology Madras (IITM)              |
            |São Paulo      |Brazil          |69  |Latin America|0    |Universidade de São Paulo                                 |
            |Melbourne      |Australia       |70  |Oceania      |0    |Monash University                                         |
            |New Haven      |United States   |71  |North America|0    |Yale University                                           |
            |Harbin         |China (Mainland)|72  |Asia         |0    |Harbin Institute of Technology                            |
            |University Park|United States   |73  |North America|0    |Pennsylvania State University                             |
            |Pohang         |South Korea     |74  |Asia         |0    |Pohang University of Science And Technology (POSTECH)     |
            |Monterrey      |Mexico          |75  |Latin America|NULL |Tecnológico de Monterrey                                  |
            +---------------+----------------+----+-------------+-----+----------------------------------------------------------+
            
            +----------------------------------------------------------+----+
            |title                                                     |rank|
            +----------------------------------------------------------+----+
            |Tecnológico de Monterrey                                  |75  |
            |Pohang University of Science And Technology (POSTECH)     |74  |
            |Pennsylvania State University                             |73  |
            |Harbin Institute of Technology                            |72  |
            |Yale University                                           |71  |
            |Monash University                                         |70  |
            |Universidade de São Paulo                                 |69  |
            |Indian Institute of Technology Madras (IITM)              |68  |
            |Kyoto University                                          |67  |
            |Universiti Malaya (UM)                                    |66  |
            |Universitat Politècnica de Catalunya · BarcelonaTech (UPC)|65  |
            |Sorbonne University                                       |64  |
            |King Fahd University of Petroleum & Minerals              |63  |
            |University of Washington                                  |62  |
            |Universidad Nacional Autónoma de México  (UNAM)           |61  |
            +----------------------------------------------------------+----+

