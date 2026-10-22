
from record_utils import (
    calculate_date_totals,
    calculate_average_minutes,
    filter_records_by_date_range,
    calculate_date_range_total,
    calculate_date_range_average,
    calculate_date_range_summary,
    count_study_days,
    sort_subject_totals_desc
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

def show_top_subject(subject: str, minutes: int) -> None:
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
    print(f'学習日数: {summary["study_days"]}日')

def show_study_days(records: list[Record]) -> None:
    result = count_study_days(records)
    print(f'学習日数: {result}日')

def show_records(records):
    if not records:
        print('記録がありません')
        return
    for record in records:
        print(f'日付:{record["date"]},科目:{record["subject"]},学習時間:{record["minutes"]}分')

def show_numbered_records(records):
    if not records:
        print('記録がありません')
        return
    for number, record in enumerate(records, start=1):
        print(f'{number}.日付:{record["date"]},科目:{record["subject"]},学習時間:{record["minutes"]}分')

def show_menu():
    print('---------------')
    print('1.学習記録を見る')
    print('2.学習記録を追加する')
    print('3.科目から検索する')
    print('4.合計学習時間を見る')
    print('5.科目ごとの合計学習時間を見る')
    print('6.データを保存する')
    print('7.学習記録を削除する')
    print('8.学習記録を編集する')
    print('9.指定した科目の合計時間を見る')
    print('10.最も学習時間が長い科目を見る')
    print('11.科目別ランキングを見る')
    print('12.日付から記録を検索する')
    print('13.指定した日付の合計学習時間を見る')
    print('14.指定した日の科目別学習時間を見る')
    print('15.指定した日付と科目の記録を見る')
    print('16.日付ごとの学習一覧')
    print('17.平均学習時間を見る')
    print('18.最も学習した科目を見る')
    print('19.期間を指定して学習記録を見る')
    print('20.期間内の合計学習時間を見る')
    print('21.期間内の平均学習時間を見る')
    print('22.期間内の学習サマリーを見る')
    print('23.学習日数を見る')
    print('24.CSVに書き出す')
    print('25.期間内の科目別ランキングを見る')
    print('0.終了')
    print('----------------')

def show_total_minutes(total: int) -> None:
    print(f'合計学習時間:{total}分')

def show_subject_totals(totals: dict[str, int]) -> None:
    print('科目別合計学習時間')
    for subject in totals:
        print(f'{subject}:{totals[subject]}分')

def show_selected_subject_total(subject: str, total:int) -> None:
    print(f'{subject}の合計学習時間:{total}分')

def show_date_total(date: str, total:int) -> None:
    print(f'{date}の合計学習時間:{total}分')

def show_date_subject_totals(date: str,totals: dict[str, int]) -> None:
    print(f'{date}の科目別学習時間')
    for subject in totals:
        print(f'{subject}:{totals[subject]}分')

def show_subject_ranking(totals: list[tuple[str, int]]) -> None:
    for number, (subject, minutes) in enumerate(totals, start=1):
        print(f'{number}位 {subject}:{minutes}分')

def show_date_range_subject_ranking_header(start_date: str, end_date: str) -> None:
    print(f'{start_date} ～ {end_date} の科目別ランキング')

