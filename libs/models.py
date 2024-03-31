from typing import Dict, Union, Optional
from pydantic import BaseModel, validator, Field, TypeAdapter
from comp import BroadSubArea, PublicHoliday, UniRank, UniWebEmail


class DataUni(BaseModel):
    title: str = None
    region: str = None
    stars: str = None
    country: str = None
    city: str = None
    rank: str = None
    rank_19: str = None
    score: str = None
    name: BroadSubArea

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
