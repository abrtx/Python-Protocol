from typing import Protocol
from dataclasses import dataclass
import httpx


class WebScrap(Protocol):
    '''Protocol for Scrap classes'''

    def download_json(self):
        '''Download data from web API'''
        
