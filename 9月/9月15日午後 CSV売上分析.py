import csv

def load_sales_from_csv():
    with open("sales.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        sales = []
        for row in reader:
            price =int(row["price"])
            quantity = int(row["quantity"])
            sales.append({
                "name":row["name"], "price":price, "quantity":quantity
            })
    return sales

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def input_positive_integer(message):
    while True:
        number = input_integer(message)
        if number > 0:
            return number
        else:
            print('1以上で入力してください')

def calculate_total_sales(sales):
    total = 0
    for sale in sales:
        total += sale["price"] * sale["quantity"]
    return total

def calculate_sales_by_product(sales):
    totals = {}
    for sale in sales:
        if sale["name"] not in totals:
            totals[sale["name"]] = sale["price"] * sale["quantity"]
        else:
            totals[sale["name"]] += sale["price"] * sale["quantity"]
    return totals

def find_top_product(totals):
    max_name = None
    max_sales = 0
    for product_name in totals:
        if totals[product_name] > max_sales:
            max_sales = totals[product_name]
            max_name = product_name
    return max_name, max_sales

def calculate_quantity_by_product(sales):
    totals = {}
    for sale in sales:
        if sale["name"] not in totals:
            totals[sale["name"]] = sale["quantity"]
        else:
            totals[sale["name"]] += sale["quantity"]
    return totals

def find_top_quantity(quantity_totals):
    max_name = None
    max_quantity = 0
    for product_name in quantity_totals:
        if quantity_totals[product_name] > max_quantity:
            max_quantity = quantity_totals[product_name]
            max_name = product_name
    return max_name, max_quantity

def show_sales_report(sales):
    if not sales:
        print('売上データがありません')
        return
    total = calculate_total_sales(sales)
    print('-----------------')
    print(f'総売上:{total}円')
    print('-----------------')
    totals_by = calculate_sales_by_product(sales)
    print('商品別売上')
    for product_name in totals_by:
        print(f'{product_name}:{totals_by[product_name]}円')
    print('-----------------')
    top_name,top_sales = find_top_product(totals_by)
    print(f'最高売上商品:{top_name} {top_sales}円')
    quantity_totals =calculate_quantity_by_product(sales)
    top_quantity_name, top_quantity = find_top_quantity(quantity_totals)
    print(f'最多販売商品:{top_quantity_name} {top_quantity}個')

def append_sale_to_csv(name,price,quantity):
    with open("sales.csv", "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, price, quantity])

def input_sale(sales):
    name = input('商品名を入力')
    price = input_positive_integer('価格を入力')
    quantity = input_positive_integer('個数を入力')
    append_sale_to_csv(name,price,quantity)
    sales.append({
        "name":name,
        "price":price,
        "quantity":quantity
    })
    print('販売記録を追加しました')

def run_sales_analyzer(sales):
    while True :
        print('-----CSV売上分析-----')
        print('1.売上レポート')
        print('2.販売記録を追加')
        print('0.終了')
        number = input_integer('番号を入力')
        if number == 1:
            show_sales_report(sales)
        elif number == 2:
            input_sale(sales)
        elif number == 0:
            print('終了')
            break
        else:
            print('正しい番号を入力してください')


sales = load_sales_from_csv()
run_sales_analyzer(sales)


