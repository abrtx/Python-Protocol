
# Table of Contents

1.  [Python&rsquo;s Features](#orgff097cb)
2.  [SOLID principles](#org6627e7e)
    1.  [D (Dependency Inversion)](#orgae66aad)
        1.  [Python&rsquo;s Protocol](#org221175e)
        2.  [Python Example](#orgdb88e13)
3.  [OOP concepts](#org6b97310)
    1.  [Composition](#orgba0fbf5)
        1.  [Example](#org692dd06)
4.  [Libraries and utilities](#org98448e1)
    1.  [Pydantic (Library)](#orgc8232f6)
        1.  [Why use Pydantic](#orgd7cae5f)
        2.  [How to use](#org6d148cc)
    2.  [Dependency Injection (programming technique)](#org035a030)
        1.  [Why use Dependency Injection](#orgab1f5ce)
        2.  [How to use](#orgac6b0b0)
    3.  [PySpark](#org86d3ce8)
        1.  [How to use](#org28364a5)



<a id="orgff097cb"></a>

# Python&rsquo;s Features

In data projects we need to solve issues. Abstract methods, 
data modelers and data validators come to help there.
That&rsquo;s what I try to show here.


<a id="org6627e7e"></a>

# SOLID principles


<a id="orgae66aad"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="org221175e"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="orgdb88e13"></a>

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


<a id="org6b97310"></a>

# OOP concepts


<a id="orgba0fbf5"></a>

## Composition

It describes a class that references one or more objects of 
other classes in instance variables.


<a id="org692dd06"></a>

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

3.  Models

        
        from comp import BroadSubArea, PublicHoliday, UniRank, UniWebEmail
        
        
        class DataComp(BaseModel):
            comp_0: str = BroadSubArea
            comp_2: str = PublicHoliday
            comp_3: str = UniRank
            comp_4: str = UniWebEmail
        
            def test_comp_0(self):
        	return self.comp_0
        
            def test_comp_2(self):
        	return self.comp_2
        
            def test_comp_3(self):
        	return self.comp_3
        
            def test_comp_4(self):
        	return self.comp_4

4.  Main

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

5.  Outputs

        
        (scraping) abrtx@abrtx-laptop:~/work/python/web_scraping$ python main.py 
        []
        {'startDate': '2023-12-30', 'endDate': '2024-01-01'}
        {'startDate': '2024-03-29', 'endDate': '2024-03-31'}
        {'startDate': '2024-05-18', 'endDate': '2024-05-21'}
        {'startDate': '2024-06-20', 'endDate': '2024-06-24'}
        {'startDate': '2024-07-13', 'endDate': '2024-07-16'}
        {'startDate': '2024-08-15', 'endDate': '2024-08-18'}
        {'startDate': '2024-09-18', 'endDate': '2024-09-22'}
        {'startDate': '2024-10-31', 'endDate': '2024-11-03'}
        (scraping) abrtx@abrtx-laptop:~/work/python/web_scraping$ python main.py 
        ['subjects', 'Broad subject area']
        {'name': 'Arts and Humanities', 'url': '/university-subject-rankings/arts-humanities'}
        {'name': 'Engineering and Technology', 'url': '/university-subject-rankings/engineering-technology'}
        {'name': 'Life Sciences and Medicine', 'url': '/university-subject-rankings/life-sciences-medicine'}
        {'name': 'Natural Sciences', 'url': '/university-subject-rankings/natural-sciences'}
        {'name': 'Social Sciences and Management', 'url': '/university-subject-rankings/social-sciences-management'}
        (scraping) abrtx@abrtx-laptop:~/work/python/web_scraping$ python main.py 
        ['data']
        {}
        {}
        {'uni_website': 'https://escp.eu/?utm_source=qs-topuniversities&utm_medium=programmeReferencing-referral&utm_campaign=fed_mk', 'uni_email': 'mimmadrid@escp.eu'}
        {'uni_website': 'http://unex.uci.edu/international/certificates/overview.aspx', 'uni_email': 'jsices@uci.edu'}
        {}
        {'uni_website': 'http://www.nyit.edu/canada'}
        {'uni_website': 'https://www.rhsmith.umd.edu/', 'uni_email': 'SmithMasters@umd.edu'}
        {}
        {'uni_website': 'https://lallyschool.rpi.edu/'}
        {'uni_website': 'http://robinson.gsu.edu/'}
        (scraping) abrtx@abrtx-laptop:~/work/python/web_scraping$ python main.py 
        ['score_nodes']
        {
            'title': 'Massachusetts Institute of Technology (MIT) ',
            'path': '/universities/massachusetts-institute-technology-mit',
            'region': 'North America',
            'country': 'United States',
            'city': 'Cambridge',
            'overall_score': '96.3'
        }
        {
            'title': 'Carnegie Mellon University',
            'path': '/universities/carnegie-mellon-university',
            'region': 'North America',
            'country': 'United States',
            'city': 'Pittsburgh',
            'overall_score': '95.9'
        }
        (scraping) abrtx@abrtx-laptop:~/work/python/web_scraping$ 


<a id="org98448e1"></a>

# Libraries and utilities


<a id="orgc8232f6"></a>

## Pydantic (Library)

Pydantic allows custom validators and serializers to alter 
how data is processed in many powerful ways.
More information <https://docs.pydantic.dev/latest/>


<a id="orgd7cae5f"></a>

### Why use Pydantic

For scraping example, there is a field that is in blank
from API, and sometimes we need to set a default value. 
We could to define a BaseModel, feature from Pydantic 
library, and add that validator.


<a id="org6d148cc"></a>

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


<a id="org035a030"></a>

## Dependency Injection (programming technique)

An object or function receives other objects or 
functions instead of creating it.


<a id="orgab1f5ce"></a>

### Why use Dependency Injection

Because it helps to decrease coupling and increase 
cohesion. Those metrics are often inversely correlated.
We need to procure low coupling and high cohesion. 


<a id="orgac6b0b0"></a>

### How to use

In the previous example we can see it was applied.
Here we can see that download<sub>json</sub> function receive
WebScrap instead of create it.

    from libs.protocols import WebScrap
    
    
    class ScrapProcessor:
    
        def download_json(self,webS: WebScrap):
    	return webS.download_json()


<a id="org86d3ce8"></a>

## PySpark

PySpark is the Python API for Apache Spark. 
It enables you to perform real-time, large-scale 
data processing in a distributed environment using Python.
For more information: <https://spark.apache.org/docs/latest/api/python/index.html#:~:text=PySpark%20is%20the%20Python%20API,for%20interactively%20analyzing%20your%20data>.


<a id="org28364a5"></a>

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

