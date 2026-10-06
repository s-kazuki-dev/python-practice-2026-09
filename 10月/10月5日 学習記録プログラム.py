import json

from pathlib import Path
DATA_FILE = Path(__file__).parent / "records.json"

def load_records():
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as file:
            records = json.load(file)
            return records
    except FileNotFoundError:
        return []

def save_records(records):
    with open(DATA_FILE,"w",encoding="utf-8") as file:
        json.dump(records,file,ensure_ascii=False,indent=4)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_records(records):
    if not records:
        print('記録がありません')
        return
    for record in records:
        print(f'科目:{record["subject"]},学習時間:{record["minutes"]}分')

def show_numbered_records(records):
    if not records:
        print('記録がありません')
        return
    for number, record in enumerate(records, start=1):
        print(f'{number}.科目:{record["subject"]},学習時間:{record["minutes"]}分')

def add_records(records, subject, minutes):
    records.append({
        "subject":subject,
        "minutes":minutes
    })

def input_add_records(records):
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
    add_records(records, subject, minutes)
    print('追加しました')
    show_records(records)

def search_records(records):
    if not records:
        print('記録がありません')
        return
    keyword = input('科目名を入力/0で中止:')
    if keyword == "0":
        return
    searched_records = []
    for record in records:
        if keyword in record["subject"]:
            searched_records.append(record)
    if not searched_records:
        print('検索された科目の記録はありません')
        return
    show_records(searched_records)

def show_total_minutes(records):
    if not records:
        print('記録がありません')
        return
    totals = 0
    for record in records:
        totals += record["minutes"]
    print(f'合計学習時間:{totals}分')

def calculate_subject_totals(records):
    totals = {}
    for record in records:
        if record["subject"] not in totals:
            totals[record["subject"]] = record["minutes"]
        else:
            totals[record["subject"]] += record["minutes"]
    return totals

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
                print('1.科目名を変更')
                print('2.学習時間を変更')
                print('0.中止')
                print('--------------')
                number = input_integer('番号を入力')
                if number == 0:
                    print('中止します')
                    return
                elif number == 1:
                    subject = input('新しい科目名を入力:')
                    records[edit_number-1]["subject"] = subject
                    print('変更しました')
                    return
                elif number == 2:
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
        elif number == 0:
            save_records(records)
            print('データを保存して終了します')
            break
        else:
            print('正しい番号を入力してください')


records = load_records()
run_menu(records)
