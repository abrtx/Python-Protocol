import httpx
import json

class ScrapTopUniversity:

    def download_json(self,url):

        self.resp = httpx.get(url)

        for node in self.resp.json()['score_nodes']:
            yield node
        


