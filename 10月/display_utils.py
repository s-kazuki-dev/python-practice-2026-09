
from record_utils import (
    calculate_date_totals,
    calculate_average_minutes
)

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
