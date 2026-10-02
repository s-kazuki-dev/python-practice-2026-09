import json

def load_expenses():
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            loaded_expenses = json.load(file)
            return loaded_expenses
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)
        
def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_expenses(expenses):
    if not expenses:
        print('支出がありません')
        return
    for number, expense in enumerate(expenses, start=1):
        print(f'{number}. {expense["name"]}:{expense["price"]}円:({expense["category"]}:{expense["memo"]})')

def add_expense(expenses,name,price,category,memo):
    expenses.append({
        "name":name,
        "price":price,
        "category":category,
        "memo":memo
    })
    save_expenses(expenses)

def input_add_expense(expenses):
    while True:
        name = input('項目名を入力/「中止」と入力でキャンセル:').strip()
        if not name:
            print('項目を入力:')
        elif name == "中止":
            return
        else:
            break
    while True:
        price = input_integer('金額を入力/0でキャンセル:')
        if price == 0:
            return
        elif price < 0:
            print('正しい金額を入力してください')
        else:
            break
    while True:
        category = input('カテゴリを入力/「中止」と入力でキャンセル:').strip()
        if not category:
            print('カテゴリを入力:')
        elif category == "中止":
            return
        else:
            break
    memo = input('メモを入力/「中止」と入力でキャンセル:').strip()
    if memo == "中止":
        return
    add_expense(expenses,name,price,category,memo)
    print('追加しました')

def show_totals(expenses):
    if not expenses:
        print('支出がありません')
        return
    totals = 0
    for expense in expenses:
        totals += expense["price"]
    print(f'合計金額:{totals}円')

def show_each_totals(expenses):
    if not expenses:
        print('支出がありません')
        return
    totals = {}
    for expense in expenses:
        if expense["category"] not in totals:
            totals[expense["category"]] = expense["price"]
        else:
            totals[expense["category"]] += expense["price"]
    for category in totals:
        print(f'{category}: {totals[category]}円')

def delete_expenses(expenses, delete_number):
    del expenses[delete_number-1]
    save_expenses(expenses)

def input_delete_expenses(expenses):
    if not expenses:
        print('支出がありません')
        return
    while True:
        show_expenses(expenses)
        number = input_integer('削除する番号を入力/0でキャンセル:')
        if number == 0:
            return
        elif 1 <= number <= len(expenses):
            delete_expenses(expenses,number)
            break
        else:
            print('正しい番号を入力してください')
    print('削除しました')
    show_expenses(expenses)

def run_menu(expenses):
    while True:
        print('------------')
        print('1.支出一覧')
        print('2.支出追加')
        print('3.合計金額')
        print('4.カテゴリ別合計金額')
        print('5.支出削除')
        print('0.終了')
        print('------------')
        number = input_integer('番号を入力')
        if number == 1:
            show_expenses(expenses)
        elif number == 2:
            input_add_expense(expenses)
        elif number == 3:
            show_totals(expenses)
        elif number == 4:
            show_each_totals(expenses)
        elif number == 5:
            input_delete_expenses(expenses)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

expenses = load_expenses()
run_menu(expenses)

