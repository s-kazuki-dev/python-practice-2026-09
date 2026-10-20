
from record_types import Record, DateRangeSummary

from typing import Literal

from datetime import datetime

#科目ごとの絞り込み
def filter_records_by_subject(records: list[Record], keyword: str) -> list[Record]:
    filtered_records = [
        record for record in records
        if keyword in record["subject"]
    ]
    return filtered_records

#日付ごとの絞り込み
def filter_records_by_date(records: list[Record], date: str) -> list[Record]:
    filtered_records = [
        record for record in records
        if record["date"] == date
    ]
    return filtered_records

#合計学習時間
def calculate_total_minutes(records: list[Record]) -> int:
    return sum(record["minutes"] for record in records)

#合計学習時間(科目ごと)
def calculate_subject_totals(records: list[Record]) -> dict[str, int]:
    return calculate_totals_by_key(records, "subject")

def calculate_average_minutes(records: list[Record]) -> float:
    if not records:
        return 0
    total = calculate_total_minutes(records)
    average = total / len(records)
    return average

def calculate_date_total(records: list[Record], date: str) -> int:
    filtered_records = filter_records_by_date(records, date)
    total = calculate_total_minutes(filtered_records)
    return total

def calculate_date_totals(records: list[Record]) -> dict[str, int]:
    return calculate_totals_by_key(records, "date")
    
def calculate_totals_by_key(records: list[Record], key: Literal["subject", "date"]) -> dict[str, int]:
    totals = {}
    for record in records:
        totals[record[key]] = totals.get(record[key], 0) + record["minutes"]
    return totals

def find_top_subject(records: list[Record]) -> tuple[str, int] | None:
    if not records:
        return None
    result = calculate_subject_totals(records)
    max_subject = max(result, key=lambda subject: result[subject])
    return (max_subject, result[max_subject])
    
def filter_records_by_date_range(records: list[Record], start_date: str, end_date: str) -> list[Record]:
    result = [
        record for record in records 
        if start_date <= record["date"] <= end_date
    ]
    return result

def calculate_date_range_total(records: list[Record], start_date: str, end_date: str) -> int:
    result = filter_records_by_date_range(records, start_date, end_date)
    total = calculate_total_minutes(result)
    return total

def calculate_date_range_average(records: list[Record], start_date: str, end_date: str) -> float:
    result = filter_records_by_date_range(records, start_date, end_date)
    average = calculate_average_minutes(result)
    return average

def calculate_date_range_summary(records: list[Record], start_date: str, end_date: str) -> DateRangeSummary | None:
    result = filter_records_by_date_range(records, start_date, end_date)
    if not result:
        return None
    study_days = count_study_days(result)
    total = calculate_total_minutes(result)
    average = calculate_average_minutes(result)
    top_record = find_top_subject(result)
    if top_record is None:
        return None
    top_subject, top_minutes = top_record
    return {
        "total": total,
        "average": average,
        "top_subject": top_subject,
        "top_minutes": top_minutes,
        "study_days": study_days
    }

def count_study_days(records: list[Record]) -> int:
    dates: set[str] = {
        record["date"] for record in records
    }
    count = len(dates)
    return count

def convert_minutes_to_hours(totals: dict[str, int]) -> dict[str, float]:
    result = {
        subject: minutes / 60 for subject, minutes in totals.items()
    }
    return result

def has_subject(records: list[Record], subject: str) -> bool:
    return any(record["subject"] == subject for record in records)
    
def all_records_have_positive_minutes(records: list[Record]) -> bool:
    return all(record["minutes"] > 0 for record in records)
    
def find_first_record_by_subject(records: list[Record], subject: str) -> Record | None:
    return next((record for record in records if record["subject"] == subject), None)

def sort_records_by_minutes(records: list[Record], *,  reverse: bool = False) -> list[Record]:
    return sorted(records, key=lambda record: record["minutes"], reverse=reverse)

def sort_records_by_date_and_minutes(records: list[Record]) -> list[Record]:
    return sorted(records, key=lambda record: (record["date"], record["minutes"]))

def validate_minutes(minutes: int) -> None:
    if minutes < 0:
        raise ValueError("学習時間は0以上にしてください")

def validate_subject(subject: str) -> None:
    if subject.strip() == "":
        raise ValueError("科目名を入力してください")

def validate_date(date: str) -> None:
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("日付はYYYY-MM-DD形式で入力してください")
    if parsed_date.strftime("%Y-%m-%d") != date:
        raise ValueError("日付はYYYY-MM-DD形式で入力してください")

def create_record(date: str, subject: str, minutes: int) -> Record:
    normalized_subject = normalize_subject(subject)
    validate_minutes(minutes)
    validate_subject(normalized_subject)
    validate_date(date)
    record: Record = {
        "date": date,
        "subject": normalized_subject,
        "minutes": minutes
    }
    return record

def normalize_subject(subject: str) -> str:
    normalized_subject = subject.strip()
    return normalized_subject

