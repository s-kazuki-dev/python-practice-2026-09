import json

def load_records():
    try:
        with open("records.json", "r", encoding="utf-8") as file:
            loaded_records = json.load(file)
            return loaded_records
    except FileNotFoundError:
        return []

def save_records(records):
    with open("records.json", "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def positive_input_integer(message):
    while True:
        number = input_integer(message)
        if number < 1:
            print('1以上で入力してください')
            continue
        return number

def show_records(records):
    if not records:
        print('学習記録がありません')
        return
    for number,record in enumerate(records,start=1):
        print(f'{number}.{record["subject"]}:{record["minutes"]}分:{record["memo"]}')

def total_records(records):
    if not records:
        print('学習記録がありません')
        return
    total = 0
    for record in records:
        total += record["minutes"]
    print('合計学習時間')
    print(f'{total}分')

def each_total_records(records):
    if not records:
        print('学習記録がありません')
        return
    totals = {}
    for record in records:
        if record["subject"] not in totals:
            totals[record["subject"]] = record["minutes"]
        else:
            totals[record["subject"]] += record["minutes"]
    for subject in totals:
        print(f'{subject}:{totals[subject]}分')

def add_records(records,subject,minutes,memo):
    records.append({
        "subject":subject,
        "minutes":minutes,
        "memo":memo
    })

def input_add_records(records):
    while True:
        subject = input('科目名を入力:').strip().lower()
        if not subject:
            print('科目名を入力してください')
            continue
        minutes = positive_input_integer('学習時間(分)を入力:')
        memo = input('メモを入力:').strip()
        add_records(records, subject, minutes, memo)
        print('追加しました')
        save_records(records)
        show_records(records)
        return

def delete_records(records,delete_number):
    del records[delete_number-1]
    print('削除しました')
    save_records(records)
    show_records(records)

def input_delete_records(records):
    if not records:
        print('学習記録はありません')
        return
    show_records(records)
    while True:
        delete_number = input_integer('削除する番号を入力/0でキャンセル:')
        if delete_number == 0:
            return
        elif 1 <= delete_number <= len(records):
            delete_records(records,delete_number)
            return
        else:
            print('正しい番号を入力してください')

def run_records_program(records):
    while True:
        print('-------------------')
        print('1.学習記録を閲覧')
        print('2.合計学習時間を確認')
        print('3.科目別学習時間を確認')
        print('4.学習記録を追加')
        print('5.学習記録を削除')
        print('0.終了')
        print('--------------------')
        number = input_integer('番号を入力:')
        if number == 1:
            show_records(records)
        elif number == 2:
            total_records(records)
        elif number == 3:
            each_total_records(records)
        elif number == 4:
            input_add_records(records)
        elif number == 5:
            input_delete_records(records)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

records = load_records()
run_records_program(records)
