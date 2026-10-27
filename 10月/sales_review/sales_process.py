
#記録ごとの売上
def calculate_sales(price: int, quantity: int) -> int:
    amount = price * quantity
    return amount

#全体の売上
def calculate_total_sales(datas) -> int:
    totals = 0
    for data in datas:
        totals += calculate_sales(data["price"], data["quantity"])
    return totals

#全体の販売数量
def calculate_total_quantity(datas) -> int:
    totals = 0
    for data in datas:
        totals += data["quantity"]
    return totals

#keyごとの売上
def calculate_total_sales_by_key(datas, key: str) -> dict[str, int]:
    totals = {}
    for data in datas:
        totals[data[key]] = totals.get(data[key], 0) + calculate_sales(data["price"], data["quantity"])
    return totals

#商品ごとの売上
def calculate_total_sales_by_product(datas) -> dict[str, int]:
    total_sales_by_product = calculate_total_sales_by_key(datas, "name")
    return total_sales_by_product

#日付ごとの売上
def calculate_total_sales_by_date(datas) -> dict[str, int]:
    total_sales_by_date = calculate_total_sales_by_key(datas, "date")
    return total_sales_by_date

#keyごとの販売数量
def calculate_total_quantity_by_key(datas, key: str) -> dict[str, int]:
    totals = {}
    for data in datas:
        totals[data[key]] = totals.get(data[key], 0) + data["quantity"]
    return totals
    
#商品ごとの販売数量
def calculate_total_quantity_by_product(datas) -> dict[str, int]:
    total_quantity_by_product = calculate_total_quantity_by_key(datas, "name")
    return total_quantity_by_product

#日付ごとの販売数量
def calculate_total_quantity_by_date(datas) -> dict[str, int]:
    total_quantity_by_date = calculate_total_quantity_by_key(datas, "date")
    return total_quantity_by_date

#商品ごとの売上ランキング
def sorted_total_sales_ranking_by_product(datas, reverse=False) -> list[tuple[str, int]]:
    totals = calculate_total_sales_by_product(datas)
    ranking = sorted(totals.items(), key=lambda item: item[1], reverse=reverse)
    return ranking

#日付ごとの売上ランキング
def sorted_total_sales_ranking_by_date(datas, reverse=False) -> list[tuple[str, int]]:
    totals =calculate_total_sales_by_date(datas)
    ranking = sorted(totals.items(), key=lambda item: item[1], reverse=reverse)
    return ranking

#売上ランキング(同率順位あり)
def add_competition_rank(ranking: list[tuple[str, int]]) -> list[tuple[int, str, int]]:
    previous_sales = None
    rank = 0
    ranked_data = []
    for number, (product, sales) in enumerate(ranking, start=1):
        if previous_sales != sales:
            rank = number
        ranked_data.append((rank, product, sales))
        previous_sales = sales
    return ranked_data

#売上最高日とその金額
def calculate_max_sales_date(datas) -> list[tuple[str, int]]:
    ranking = sorted_total_sales_ranking_by_date(datas, reverse=True)
    ranked_data = add_competition_rank(ranking)
    max_sales_date = []
    for data in ranked_data:
        if data[0] == 1:            #date[0]は順位
            max_sales_date.append(
            (data[1], data[2]) #date[1]は日付, date[2]は金額
            )
    return max_sales_date

#売上最低日とその金額
def calculate_min_sales_date(datas) -> list[tuple[str, int]]:
    ranking = sorted_total_sales_ranking_by_date(datas)
    ranked_data = add_competition_rank(ranking)
    min_sales_date = []
    for data in ranked_data:
        if data[0] == 1:
            min_sales_date.append(
            (data[1], data[2])
            )
    return min_sales_date

#売上最高日 - 売上最低日　の差額
def calculate_difference_by_date(datas) -> int:
    max_sales_date = calculate_max_sales_date(datas)
    max_sales = max_sales_date[0][1]
    min_sales_date = calculate_min_sales_date(datas)
    min_sales = min_sales_date[0][1]
    return max_sales - min_sales

#新しいデータの追加
def add_new_data(datas, date, product, price, quantity):
    datas.append(
        {"date": date, "name": product, "price": price, "quantity": quantity}
    )
    return datas



