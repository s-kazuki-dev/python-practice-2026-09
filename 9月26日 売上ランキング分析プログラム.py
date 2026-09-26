sales = [
    {"product": "コーヒー", "price": 150, "quantity": 3},
    {"product": "お茶", "price": 120, "quantity": 5},
    {"product": "コーヒー", "price": 150, "quantity": 2},
    {"product": "水", "price": 100, "quantity": 4},
    {"product": "お茶", "price": 120, "quantity": 1}
]

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください:')

def total_sale(sales):
    if not sales:
        print('記録がありません')
        return
    total = 0
    for sale in sales:
        total += sale["price"] * sale["quantity"]
    print(f'{total}円')

def each_product(sales):
    if not sales:
        print('記録がありません')
        return
    totals = {}
    for sale in sales:
        if sale["product"] not in totals:
            totals[sale["product"]] = {
                "price":sale["price"] * sale["quantity"],
                "counts":sale["quantity"]
            }
            
        else:
            totals[sale["product"]]["price"] += sale["price"] * sale["quantity"]
            totals[sale["product"]]["counts"] += sale["quantity"]
    
    return totals

def show_rank(sales):
    total = each_product(sales)
    sorted_sales = sorted(total.items(), key=lambda item:item[1]["price"], reverse=True)
    for number,sorted_sale in enumerate(sorted_sales, start=1) :
        print(f'{number}. {sorted_sale[0]}:{sorted_sale[1]["price"]}円')

def counts_top(sales):
    totals = each_product(sales)
    top_name = None
    top_counts = 0
    for product in totals:
        if totals[product]["counts"] > top_counts:
            top_counts = totals[product]["counts"]
            top_name = product
    print(f'販売数トップ:{top_name}/{top_counts}個')

def run_menu(sales):
    while True:
        print('---------------')
        print('1.全体売上')
        print('2.商品別集計')
        print('3.売上ランキング')
        print('4.販売数トップ')
        print('0.終了')
        print('----------------')
        number = input_integer('番号を入力')
        if number == 1:
            total_sale(sales)
        elif number == 2:
            totals = each_product(sales)
            for product in totals:
                    print(f'{product}:{totals[product]["counts"]}個/{totals[product]["price"]}円')
        elif number == 3:
            show_rank(sales)
        elif number == 4:
            counts_top(sales)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

run_menu(sales)


