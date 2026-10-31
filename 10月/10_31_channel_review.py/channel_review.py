sales_datas = [
    {"date": "2026-10-28", "channel": "店内", "name": "コーヒー", "price": 400, "quantity": 3},
    {"date": "2026-10-28", "channel": "テイクアウト", "name": "コーヒー", "price": 400, "quantity": 2},
    {"date": "2026-10-28", "channel": "店内", "name": "カレー", "price": 900, "quantity": 2},
    {"date": "2026-10-29", "channel": "デリバリー", "name": "カレー", "price": 1000, "quantity": 3},
    {"date": "2026-10-29", "channel": "テイクアウト", "name": "ケーキ", "price": 500, "quantity": 4},
    {"date": "2026-10-29", "channel": "デリバリー", "name": "コーヒー", "price": 450, "quantity": 2}
]


def total_sales_and_quantity(sales_datas):
    total_sales = 0
    total_quantity = 0
    for data in sales_datas:
        total_sales += data["price"] * data["quantity"]
        total_quantity += data["quantity"]
    return total_sales, total_quantity

def total_sales_and_quantity_by_channel(sales_datas):
    totals_sales = {}
    totals_quantity = {}
    for data in sales_datas:
        totals_sales[data["channel"]] = totals_sales.get(data["channel"], 0) + data["price"] * data["quantity"]
        totals_quantity[data["channel"]] = totals_quantity.get(data["channel"], 0) + data["quantity"]
    return totals_sales, totals_quantity

def sales_ranking_by_channel(sales_datas):
    result = total_sales_and_quantity_by_channel(sales_datas)
    totals_sales, _ = result
    sorted_sales = sorted(totals_sales.items(), key=lambda item: item[1], reverse=True)
    return sorted_sales

def add_competition(sales_datas):
    sorted_sales = sales_ranking_by_channel(sales_datas)
    rank = 0
    previous_sales = None
    ranked_data = []
    for number, (channel, sales) in enumerate(sorted_sales, start=1):
        if previous_sales != sales:
            rank = number
        ranked_data.append((rank, channel, sales))
        previous_sales = sales
    return ranked_data  
    
def show_totals(total_sales, total_quantity):
    print('全体の売上金額と販売数量')
    print(f'{total_sales}円 {total_quantity}個')

def show_totals_by_channel(totals_sales, totals_quantity):
    print('販売チャネルごとの売上金額と販売数量')
    for data in totals_sales:
        print(f'{data}: {totals_sales[data]}円 {totals_quantity[data]}個')

def show_sales_ranking_by_channel(ranked_data):
    for data in ranked_data:
        print(f'{data[0]}位: {data[1]} {data[2]}円')

def show_result(sales_datas):
    if not sales_datas:
        print('記録がありません')
        return
    total_sales, total_quantity = total_sales_and_quantity(sales_datas)
    show_totals(total_sales, total_quantity)

    totals_sales, totals_quantity = total_sales_and_quantity_by_channel(sales_datas)
    show_totals_by_channel(totals_sales, totals_quantity)

    ranked_data = add_competition(sales_datas)
    show_sales_ranking_by_channel(ranked_data)



if __name__ == "__main__":
    show_result(sales_datas)
