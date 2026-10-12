from datetime import datetime

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def input_date(message):
    while True:
        try:
            date = input(message)
            if date == "0":
                print('中止しました')
                return None
            datetime.strptime(date,"%Y-%m-%d")
            return date
        except ValueError:
            print('正しい日付を入力してください')

def input_date_range():
    start_date = input_date('開始日を入力してください/0で中止')
    if start_date is None:
        print('処理を中止しました')
        return None
    end_date = input_date('終了日を入力してください/0で中止')
    if end_date is None:
        print('処理を中止しました')
        return None
    if start_date > end_date:
        print('開始日は終了日以前の日付を入力してください')
        return None
    return (start_date, end_date)

