
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

#商品ごとの売上
def calculate_total_sales_by_product(datas) -> dict[str, int]:
    totals = {}
    for data in datas:
        if data["name"] not in totals:
            totals[data["name"]] = calculate_sales(data["price"], data["quantity"])
        else:
            totals[data["name"]] += calculate_sales(data["price"], data["quantity"])
    return totals

#商品ごとの販売数量
def calculate_total_quantity_by_product(datas) -> dict[str, int]:
    totals = {}
    for data in datas:
        if data["name"] not in totals:
            totals[data["name"]] = data["quantity"]
        else:
            totals[data["name"]] += data["quantity"]
    return totals

