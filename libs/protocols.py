from typing import Protocol


class WebScrap(Protocol):
    '''Protocol for Scraping classes'''

    def download_json(self):
        '''Download data from web API'''
