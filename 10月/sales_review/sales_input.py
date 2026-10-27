
#数字で入力
def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

#1以上で入力
def input_positive_integer(message):
    while True:
        number = input_integer(message)
        if number > 0:
            return number
        else:
            print('1以上で入力してください')

#0以上で入力
def input_non_negative_integer(message):
    while True:
        number = input_integer(message)
        if number >= 0:
            return number
        
        else:
            print('0以上で入力してください')

#文字列を入力(空欄は再入力)
def input_str(message):
    while True:
        answer = input(message).strip()
        if not answer:
            print('入力してください')
        elif answer == "0":
            print('中止しました')
            return None
        else:
            return answer

#新データを入力
def input_new_data():
    date = input_str('日付を入力/0で中止:')
    if date is None:
        return
    product = input_str('商品名を入力/0で中止:')
    if product is None:
        return
    price = input_non_negative_integer('単価を入力')
    quantity = input_positive_integer('販売数量を入力')
    return (date, product, price, quantity)




