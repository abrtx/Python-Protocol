
# Table of Contents

1.  [SOLID principles](#orgbf58035)
    1.  [D (Dependency Inversion)](#orgef140a3)
        1.  [Python&rsquo;s Protocol](#org4687ca6)
        2.  [Python Example](#org503d25f)



<a id="orgbf58035"></a>

# SOLID principles


<a id="orgef140a3"></a>

## D (Dependency Inversion)

Classes depend on abstract classes (Python Protocols) 
not on specific classes


<a id="org4687ca6"></a>

### Python&rsquo;s Protocol

allow structural subtyping — checking whether two 
classes are compatible based on available attributes 
and functions alone.


<a id="org503d25f"></a>

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

