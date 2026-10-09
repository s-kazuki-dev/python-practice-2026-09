
from storage_utils import(
    load_records,
    save_records
)

from datetime import datetime

from record_utils import(
    filter_records_by_subject,
    filter_records_by_date,
    calculate_total_minutes,
    calculate_subject_totals,
    calculate_date_totals
)

from display_utils import (
    show_date_totals,
    show_average_minutes
)
from input_utils import(
    input_integer,
    input_date
)

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

def add_records(records, date, subject, minutes):
    records.append({
        "date":date,
        "subject":subject,
        "minutes":minutes
    })

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
    add_records(records, date, subject, minutes)
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
    
def show_total_minutes(records):
    if not records:
        print('記録がありません')
        return
    total = calculate_total_minutes(records)
    print(f'合計学習時間:{total}分')

def show_subject_totals(records):
    if not records:
        print('記録がありません')
        return
    totals = calculate_subject_totals(records)
    print(f'科目別合計学習時間')
    for subject in totals:
        print(f'{subject}:{totals[subject]}分')

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
            deleted_record = records[number-1]
            del records[number-1]
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
                    records[edit_number-1]["date"] = date
                    print('変更しました')
                    return
                elif number == 2:
                    subject = input('新しい科目名を入力:')
                    records[edit_number-1]["subject"] = subject
                    print('変更しました')
                    return
                elif number == 3:
                    while True:
                        minutes = input_integer('新しい学習時間を入力:')
                        if minutes >= 1:
                            records[edit_number-1]["minutes"] = minutes
                            print('変更しました')
                            return
                        else:
                            print('正しい学習時間を入力してください')
                else:
                    print('正しい番号を入力してください')
        else:
            print('正しい番号を入力してください')

def show_selected_subject_total(records):
    if not records:
        print('記録がありません')
        return
    subject = input('集計する科目名を入力/0で中止:')
    if subject == "0":
        print('中止しました')
        return
    totals = calculate_subject_totals(records)
    if subject in totals:
        print(f'{subject}の合計学習時間:{totals[subject]}分')
    else:
        print('その科目の記録はありません')

def show_date_total(records):
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
    print(f'{date}の合計学習時間:{total}分')

def show_top_subject(records):
    if not records:
        print('記録がありません')
        return
    totals = calculate_subject_totals(records)
    top_subject = None
    top_minutes = 0
    for subject in totals:
        if totals[subject] > top_minutes:
            top_subject = subject
            top_minutes = totals[subject]
    print(f'最も学習時間が長い科目:{top_subject}')
    print(f'合計学習時間:{top_minutes}分')

def show_subject_ranking(records):
    if not records:
        print('記録がありません')
        return
    totals = calculate_subject_totals(records)
    for number, (subject, minutes) in enumerate(
        sorted(totals.items(), key=lambda item:item[1], reverse=True),
        start=1
        ):
        print(f'{number}位 {subject}:{minutes}分')

def show_date_subject_totals(records):
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
    results = calculate_subject_totals(filtered_records)
    print(f'{date}の科目別学習時間')
    for subject in results:
        print(f'{subject}:{results[subject]}分')

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
    print('0.終了')
    print('----------------')

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
            show_total_minutes(records)
        elif number == 5:
            show_subject_totals(records)
        elif number == 6:
            save_records(records)
            print('保存しました')
        elif number == 7:
            delete_record(records)
        elif number == 8:
            edit_record(records)
        elif number == 9:
            show_selected_subject_total(records)
        elif number == 10:
            show_top_subject(records)
        elif number == 11:
            show_subject_ranking(records)
        elif number == 12:
            search_by_date(records)
        elif number == 13:
            show_date_total(records)
        elif number == 14:
            show_date_subject_totals(records)
        elif number == 15:
            search_by_date_and_subject(records)
        elif number == 16:
            show_date_totals(records)
        elif number == 17:
            show_average_minutes(records)
        elif number == 0:
            save_records(records)
            print('データを保存して終了します')
            break
        else:
            print('正しい番号を入力してください')

if __name__ == "__main__":
    records = load_records()
    run_menu(records)


