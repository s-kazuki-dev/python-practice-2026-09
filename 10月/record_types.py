from typing import TypedDict

class Record(TypedDict):
    date: str
    subject: str
    minutes: int

class DateRangeSummary(TypedDict):
    total: int
    average: float
    top_subject: str
    top_minutes: int
    study_days: int

    
