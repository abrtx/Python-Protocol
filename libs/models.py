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
