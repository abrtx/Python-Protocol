import httpx
import json

class ScrapTopUniversity:
    ''' Web Scraping '''

    def download_json(self,url):

        self.resp = httpx.get(url)

        for node in self.resp.json()['score_nodes']:
            yield node
        


