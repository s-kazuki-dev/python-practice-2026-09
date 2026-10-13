
from record_utils import (
    calculate_date_totals,
    calculate_average_minutes,
    find_top_subject,
    filter_records_by_date_range,
    calculate_date_range_total,
    calculate_date_range_average,
    calculate_total_minutes,
    calculate_date_range_summary
)

from record_types import Record


def show_date_totals(records):
    totals = calculate_date_totals(records)
    if not totals:
        print('記録がありません')
        return
    for date, total in totals.items():
        print(f'{date}: {total}分') 

def show_average_minutes(records):
    if not records:
        print('記録がありません')
        return
    average = calculate_average_minutes(records)
    print(f'平均学習時間: {average}分')

def show_top_subject(records):
    result = find_top_subject(records)
    if result is None:
        print('記録がありません')
        return
    subject, minutes = result
    print(f'最も学習した科目: {subject} ({minutes}分)')

def show_records_by_date_range(records: list[Record], start_date: str, end_date: str) -> None:
    result = filter_records_by_date_range(records, start_date, end_date)
    if not result:
        print('該当する記録がありません')
        return
    for record in result:
        print(f'{record["date"]} {record["subject"]} {record["minutes"]}分')

def show_date_range_total(records: list[Record], start_date: str, end_date: str) -> None:
    total = calculate_date_range_total(records, start_date, end_date)
    print(f'期間内の合計学習時間: {total}分')

def show_date_range_average(records: list[Record], start_date: str, end_date: str) -> None:
    average = calculate_date_range_average(records, start_date, end_date)
    print(f'期間内の平均学習時間: {average}分')

def show_date_range_summary(records: list[Record], start_date: str, end_date: str) -> None:
    summary = calculate_date_range_summary(records, start_date, end_date)
    if summary is None:
        print('記録がありません')
        return
    print(f'期間内の学習サマリー')
    print(f'合計学習時間: {summary["total"]}分')
    print(f'平均学習時間: {summary["average"]}分')
    print(f'最も学習した科目: {summary["top_subject"]} ({summary["top_minutes"]}分)')

