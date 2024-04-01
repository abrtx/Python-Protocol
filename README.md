
# Table of Contents

1.  [Python&rsquo;s Features](#org56733da)
2.  [SOLID principles](#org9b6a2af)
    1.  [D (Dependency Inversion)](#orgea47b17)
        1.  [Python&rsquo;s Protocol](#org352fd2b)
        2.  [Python Example](#orgc157a81)
3.  [OOP concepts](#org66eab4a)
    1.  [Composition](#orged2473a)
        1.  [Example](#org61cd94d)
4.  [Libraries and utilities](#org0defaeb)
    1.  [Pydantic (Library)](#org24617be)
        1.  [Why use Pydantic](#org3402bac)
        2.  [How to use](#orgbebd556)
    2.  [Dependency Injection (programming technique)](#org567d84b)
        1.  [Why use Dependency Injection](#org973997b)
        2.  [How to use](#org7627db1)
    3.  [PySpark](#org31be416)
        1.  [How to use](#org9904e2c)



<a id="org56733da"></a>

# Python&rsquo;s Features

In data projects we need to solve issues. Abstract methods, 
data modelers and data validators come to help there.
That&rsquo;s what I try to show here.


<a id="org9b6a2af"></a>

# SOLID principles


<a id="orgea47b17"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="org352fd2b"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="orgc157a81"></a>

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


<a id="org66eab4a"></a>

# OOP concepts


<a id="orged2473a"></a>

## Composition

It describes a class that references one or more objects of 
other classes in instance variables.


<a id="org61cd94d"></a>

### Example

1.  Downloading

    A little modification for trying to cover some posibilities.
    
        import httpx
        
        
        class ScrapTopUniversity:
            ''' Web Scraping '''
        
            def __init__(self, url, args=[]):
        	self.url = url
        	self.args = args
        
            def download_json(self):
        
        	print(self.args)
        	self.resp = httpx.get(self.url)
        
        	if len(self.args) == 0:
        	    for node in self.resp.json()[:10]:
        		yield node
        	elif len(self.args) == 1:
        	    for node in self.resp.json()[self.args[0]][:10]:
        		yield node
        	else:
        	    for node in self.resp.json()[self.args[0]][self.args[1]][:10]:
        		yield node

2.  Components

        from pydantic import BaseModel
        
        
        class EmployRank(BaseModel):
            region: str = None
            city: str = None
            rank_19: str = None
        
        
        class BroadSubArea(BaseModel):
            name: str = None
            url: str = None
        
        
        class UniWebEmail(BaseModel):
            uni_website: str | None = None
            uni_email: str | None = None
        
        
        class PublicHoliday(BaseModel):
            startDate: str = None
            endDate: str = None
        
        
        class UniRank(BaseModel):
            title: str = None
            path: str = None
            region: str = None
            country: str = None
            city: str = None
            overall_score: str = None

3.  Main

        from rich import print
        from libs.protocols import WebScrap
        from libs.modules import ScrapTopUniversity
        from libs.models import DataComp
        
        
        class ScrapProcessor:
        
            def download_json(self, webS: WebScrap):
        	return webS.download_json()
        
        
        def main():
        
            url1 = "https://www.topuniversities.com/rankings/endpoint?nid=3846272&page=0&items_per_page=2&tab="
        
            url2 = "https://www.topuniversities.com/ranking_table_ctas"
        
            url3 = "https://www.topuniversities.com/rankings/filter/endpoint?nid=3846272&tab=indicators"
            url4 = "https://date.nager.at/api/v3/LongWeekend/2024/CL"
        
            scrap = ScrapProcessor()
            top = scrap.download_json(
        	ScrapTopUniversity(
        	    # url3, ['subjects', 'Broad subject area']))  # 0
        	    url1, ['score_nodes']))  # 3
        	    # url2, ['data']))  # 4
        	    # url4, []))  # 2
        
            comp2 = DataComp().test_comp_3()
        
            item2 = [comp2(**t) for t in top]
        
            for row in item2:
        	print(row.dict(exclude_none=True))
        
        
        if __name__ == "__main__":
            main()


<a id="org0defaeb"></a>

# Libraries and utilities


<a id="org24617be"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="org3402bac"></a>

### Why use Pydantic

For scraping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="orgbebd556"></a>

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


<a id="org567d84b"></a>

## Dependency Injection (programming technique)

An object or function receives other objects or 
functions instead of creating it.


<a id="org973997b"></a>

### Why use Dependency Injection

Because it helps to decrease coupling and increase 
cohesion. Those metrics are often inversely correlated.
We need to procure low coupling and high cohesion. 


<a id="org7627db1"></a>

### How to use

In the previous example we can see it was applied.
Here we can see that download<sub>json</sub> function receive
WebScrap instead of create it.

    from libs.protocols import WebScrap
    
    
    class ScrapProcessor:
    
        def download_json(self,webS: WebScrap):
    	return webS.download_json()


<a id="org31be416"></a>

## PySpark

PySpark is the Python API for Apache Spark. 
It enables you to perform real-time, large-scale 
data processing in a distributed environment using Python.
For more information: <https://spark.apache.org/docs/latest/api/python/index.html#:~:text=PySpark%20is%20the%20Python%20API,for%20interactively%20analyzing%20your%20data>.


<a id="org9904e2c"></a>

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

