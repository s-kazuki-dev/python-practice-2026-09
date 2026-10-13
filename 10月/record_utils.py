
from record_types import Record

from typing import Literal

#科目ごとの絞り込み
def filter_records_by_subject(records: list[Record], keyword: str) -> list[Record]:
    filtered_records = []
    for record in records:
        if keyword in record["subject"]:
            filtered_records.append(record)
    return filtered_records

#日付ごとの絞り込み
def filter_records_by_date(records: list[Record], date: str) -> list[Record]:
    filtered_records = []
    for record in records:
        if record["date"] == date:
            filtered_records.append(record)
    return filtered_records

#合計学習時間
def calculate_total_minutes(records: list[Record]) -> int:
    total = 0
    for record in records:
        total += record["minutes"]
    return total

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
        if record[key] not in totals:
            totals[record[key]] = record["minutes"]
        else:
            totals[record[key]] += record["minutes"]
    return totals

def find_top_subject(records: list[Record]) -> tuple[str, int] | None:
    if not records:
        return None
    result = calculate_subject_totals(records)
    max_minutes = -1
    max_subject = ""
    for subject, minutes in result.items():
        if minutes > max_minutes:
            max_minutes = minutes
            max_subject = subject
    
    return (max_subject, max_minutes)

def filter_records_by_date_range(records: list[Record], start_date: str, end_date: str) -> list[Record]:
    result = []
    for record in records:
        if start_date <= record["date"] <= end_date:
            result.append(record)
    return result

def calculate_date_range_total(records: list[Record], start_date: str, end_date: str) -> int:
    result = filter_records_by_date_range(records, start_date, end_date)
    total = calculate_total_minutes(result)
    return total

def calculate_date_range_average(records: list[Record], start_date: str, end_date: str) -> float:
    result = filter_records_by_date_range(records, start_date, end_date)
    average = calculate_average_minutes(result)
    return average

