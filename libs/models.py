from pydantic import BaseModel, validator
from comp import BroadSubArea, BroadSpecificSubArea


class DataUni(BaseModel):
    title: str = None
    region: str = None
    stars: str = None
    country: str = None
    city: str = None
    rank: str = None
    rank_19: str = None
    score: str = None

    @validator('stars')
    @classmethod
    def stars_default(cls, value):

        if value in ('', None):
            return 0

    @validator('title')
    @classmethod
    def title_default(cls, value):

        if value in ('', None):
            return 0


class DataComp(BaseModel):
    comp_0: str = BroadSubArea()
    comp_1: str = BroadSpecificSubArea()

    def test_comp_0(self):
        return self.comp_0

    def test_comp_1(self):
        return self.comp_1
