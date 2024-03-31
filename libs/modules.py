import httpx


class ScrapTopUniversity:
    ''' Web Scraping '''

    def __init__(self, url, args=[]):
        self.url = url
        self.args = args
        # self.key0: str = args[0]
        # self.key1: str = args[1]

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
