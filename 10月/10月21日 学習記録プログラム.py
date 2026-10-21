
from storage_utils import(
    load_records,
    save_records,
    export_records_to_csv
)

from datetime import datetime

from record_utils import(
    filter_records_by_subject,
    filter_records_by_date,
    calculate_total_minutes,
    calculate_subject_totals,
    add_record,
    update_record_subject,
    update_record_minutes,
    update_record_date,
    delete_record_by_index,
    find_top_subject,
    sort_subject_totals_desc,
    calculate_subject_total
)

from display_utils import (
    show_date_totals,
    show_average_minutes,
    show_top_subject,
    show_records_by_date_range,
    show_date_range_total,
    show_date_range_average,
    show_date_range_summary,
    show_study_days,
    show_records,
    show_numbered_records,
    show_menu,
    show_total_minutes,
    show_subject_totals,
    show_selected_subject_total,
    show_date_total,
    show_date_subject_totals,
    show_subject_ranking
)
from input_utils import(
    input_integer,
    input_date,
    input_date_range
)

from collections.abc import Callable
from record_types import Record


def input_add_records(records):
    date = input_date('日付を入力(例:2026-10-06)/0で中止')
    if date is None:
        return
    subject = input('追加する科目を入力/0で中止:')
    if subject == "0":
        print('中止しました')
        return None
    while True:
        minutes = input_integer('学習時間を入力/0で中止:')
        if minutes == 0:
            print('中止しました')
            return None
        elif minutes < 0:
            print('正しい数字を入力してください')
        else:
            break
    try:
        add_record(records, date, subject, minutes)
    except ValueError as error:
        print(error)
        return
    print('追加しました')
    show_records(records)

def search_records(records):
    if not records:
        print('記録がありません')
        return
    keyword = input('科目名を入力/0で中止:')
    if keyword == "0":
        print('中止しました')
        return
    filtered_records = filter_records_by_subject(records,keyword)
    if not filtered_records:
        print('検索された科目の記録はありません')
        return
    show_records(filtered_records)

def search_by_date(records):
    if not records:
        print('記録がありません')
        return
    date = input_date('日付を入力/0で中止:')
    if date is None:
        return
    filtered_records = filter_records_by_date(records,date)
    if not filtered_records:
        print('その日付の記録はありません')
        return
    show_records(filtered_records)
   
def show_total_minutes_action(records):
    if not records:
        print('記録がありません')
        return
    total = calculate_total_minutes(records)
    show_total_minutes(total)

def show_subject_totals_action(records):
    if not records:
        print('記録がありません')
        return
    totals = calculate_subject_totals(records)
    show_subject_totals(totals)

def delete_record(records):
    if not records:
        print('記録がありません')
        return
    while True:
        show_numbered_records(records)
        number = input_integer('削除する番号を入力/0で中止:')
        if number == 0:
            print('中止しました')
            return
        elif 1 <= number <= len(records):
            deleted_record = delete_record_by_index(records, number - 1)
            print(f'{deleted_record["subject"]}の記録を削除しました')
            break
        else:
            print('正しい番号を入力してください')

def edit_record(records):
    if not records:
        print('記録がありません')
        return
    while True:
        show_numbered_records(records)
        edit_number = input_integer('編集する番号を入力/0で中止:')
        if edit_number == 0:
            print('中止しました')
            return
        elif 1 <= edit_number <= len(records):
            while True:
                print('--------------')
                print('1.日付を変更')
                print('2.科目名を変更')
                print('3.学習時間を変更')
                print('0.中止')
                print('--------------')
                number = input_integer('番号を入力:')
                if number == 0:
                    print('中止します')
                    return
                elif number == 1:
                    date = input_date('新しい日付を入力/0で中止:')
                    if date is None:
                        return
                    try:
                        update_record_date(records[edit_number-1], date)
                    except ValueError as error:
                        print(error)
                        return
                    print('変更しました')
                    return
                elif number == 2:
                    subject = input('新しい科目名を入力:')
                    try:
                        update_record_subject(records[edit_number-1], subject)
                    except ValueError as error:
                        print(error)
                        return
                    print('変更しました')
                    return
                elif number == 3:
                    minutes = input_integer('新しい学習時間を入力:')
                    try:
                        update_record_minutes(records[edit_number-1], minutes)
                    except ValueError as error:
                        print(error)
                        return
                    print('変更しました')
                    return
                else:
                    print('正しい番号を入力してください')
        else:
            print('正しい番号を入力してください')

def show_selected_subject_total_action(records):
    if not records:
        print('記録がありません')
        return
    subject = input('集計する科目名を入力/0で中止:')
    if subject == "0":
        print('中止しました')
        return
    total = calculate_subject_total(records, subject)
    if total is None:
        print('その科目の記録はありません')
    else:
        show_selected_subject_total(subject, total)

def show_date_total_action(records):
    if not records:
        print('記録がありません')
        return
    date = input_date('集計する日付を入力(例:2026-10-06)/0で中止:')
    if date is None:
        return
    filtered_records = filter_records_by_date(records,date)
    if not filtered_records:
        print('その日付の記録はありません')
        return
    total = calculate_total_minutes(filtered_records)
    show_date_total(date, total)

def show_top_subject_action(records):
    result = find_top_subject(records)
    if result is None:
        print('記録がありません')
        return
    subject, minutes = result
    show_top_subject(subject, minutes)

def show_subject_ranking_action(records):
    if not records:
        print('記録がありません')
        return
    totals = calculate_subject_totals(records)
    ranking = sort_subject_totals_desc(totals)
    show_subject_ranking(ranking)

def show_date_subject_totals_action(records):
    if not records:
        print('記録がありません')
        return
    date = input_date('日付を入力/0で中止:')
    if date is None:
        return
    filtered_records = filter_records_by_date(records, date)
    if not filtered_records:
        print('その日付の記録はありません')
        return
    results = calculate_subject_totals(filtered_records)
    show_date_subject_totals(date, results)

def search_by_date_and_subject(records):
    if not records:
        print('記録がありません')
        return
    date = input_date('日付を入力/0で中止:')
    if date is None:
        return
    subject = input('科目名を入力/0で中止:')
    if subject == "0":
        print('中止しました')
        return
    filtered_date_records = filter_records_by_date(records,date)
    if not filtered_date_records:
        print('一致する記録はありません')
        return
    filtered_records = filter_records_by_subject(filtered_date_records,subject)
    if not filtered_records:
        print('一致する記録はありません')
        return
    show_records(filtered_records)

def run_date_range_action(
    records: list[Record],
    action: Callable[[list[Record], str, str], None]
) -> None:
    date_range = input_date_range()
    if date_range is None:
        return
    start_date, end_date = date_range
    action(records, start_date, end_date)

def run_menu(records):
    while True:
        show_menu()
        number = input_integer('番号を入力:')
        if number == 1:
            show_records(records)
        elif number == 2:
            input_add_records(records)
        elif number == 3:
            search_records(records)
        elif number == 4:
            show_total_minutes_action(records)
        elif number == 5:
            show_subject_totals_action(records)
        elif number == 6:
            save_records(records)
            print('保存しました')
        elif number == 7:
            delete_record(records)
        elif number == 8:
            edit_record(records)
        elif number == 9:
            show_selected_subject_total_action(records)
        elif number == 10:
            show_top_subject_action(records)
        elif number == 11:
            show_subject_ranking_action(records)
        elif number == 12:
            search_by_date(records)
        elif number == 13:
            show_date_total_action(records)
        elif number == 14:
            show_date_subject_totals_action(records)
        elif number == 15:
            search_by_date_and_subject(records)
        elif number == 16:
            show_date_totals(records)
        elif number == 17:
            show_average_minutes(records)
        elif number == 18:
            show_top_subject_action(records)
        elif number == 19:
            run_date_range_action(records, show_records_by_date_range)
        elif number == 20:
            run_date_range_action(records, show_date_range_total)
        elif number == 21:
            run_date_range_action(records, show_date_range_average)
        elif number == 22:
            run_date_range_action(records, show_date_range_summary)
        elif number == 23:
            show_study_days(records)
        elif number == 24:
            export_records_to_csv(records)
            print('CSVに書き出しました')
        elif number == 0:
            save_records(records)
            print('データを保存して終了します')
            break
        else:
            print('正しい番号を入力してください')

if __name__ == "__main__":
    records = load_records()
    run_menu(records)

