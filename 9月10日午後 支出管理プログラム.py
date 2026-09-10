expenses = [
    {"name":"昼食", "price":800, "category":"食費"},
    {"name":"本", "price":1500, "category":"学習"},
    {"name":"コーヒー", "price":300, "category":"食費"}
]

def show_expenses(expenses):
    for i in range(len(expenses)):
        print(f'{i+1}: {expenses[i]["name"]} {expenses[i]["price"]}円 [{expenses[i]["category"]}]')

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字を入力してください')

def calculate_total(expenses):
    total = 0
    for i in range(len(expenses)):
        total += expenses[i]["price"]
    return total

def calculate_category_total(expenses, category):
    total = 0
    for i in range(len(expenses)):
        if expenses[i]["category"] == category:
            total += expenses[i]["price"]
    return total

def add_expense(expenses,name,price,category):
    expenses.append({
        "name":name,
        "price":price,
        "category":category
    })

def input_expense(expenses):
    name = input('支出名を入力')
    while True:
        price = input_integer('金額を入力')
        if price >= 1:
            break
        else:
            print('1円以上を入力してください')
    category = input('カテゴリを入力')
    add_expense(expenses,name,price,category)

def show_total(expenses):
    print(f'支出合計：{calculate_total(expenses)}円')
    
def show_category_total(expenses):
    category_name = input('カテゴリを入力してください：')
    print(f'{category_name}合計：{calculate_category_total(expenses, category_name)}円')

def run_expense_manager(expenses):
    while True:
        print('1:支出一覧')
        print('2:支出追加')
        print('3:合計表示')
        print('4:カテゴリ別合計')
        print('0:終了します')
        number = input_integer('番号を入力してください')
        if number == 1:
            show_expenses(expenses)
        elif number == 2:
            input_expense(expenses)
        elif number == 3:
            show_total(expenses)
        elif number == 4:
            show_category_total(expenses)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')



run_expense_manager(expenses)