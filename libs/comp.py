from pydantic import BaseModel


class EmployRank(BaseModel):
    region: str = None
    city: str = None
    rank_19: str = None


class BroadSubArea(BaseModel):
    name: str = None
    url: str = None


class BroadSpecificSubArea(BaseModel):
    name: str = None
    url: str = None
