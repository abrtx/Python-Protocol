import httpx


class ScrapTopUniversity:
    ''' Web Scraping '''

    def __init__(self, url):
        self.url = url

    def download_json(self):

        self.resp = httpx.get(self.url)

        for node in self.resp.json()['subjects']['Broad subject area']:  # ['score_nodes']:
            yield node
