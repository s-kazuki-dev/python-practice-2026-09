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
