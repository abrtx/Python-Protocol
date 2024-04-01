from pydantic import BaseModel


class EmployRank(BaseModel):
    region: str = None
    city: str = None
    rank_19: str = None


class BroadSubArea(BaseModel):
    name: str = None
    url: str = None


class UniWebEmail(BaseModel):
    uni_website: str | None = None
    uni_email: str | None = None


class PublicHoliday(BaseModel):
    startDate: str = None
    endDate: str = None


class UniRank(BaseModel):
    title: str = None
    path: str = None
    region: str = None
    country: str = None
    city: str = None
    overall_score: str = None
