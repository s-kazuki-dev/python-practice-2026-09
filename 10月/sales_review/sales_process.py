def calculate_sales(price: int, quantity: int) -> int:
    amount = price * quantity
    return amount

def calculate_total_sales(datas) -> int:
    totals = 0
    for data in datas:
        amount = calculate_sales(data["price"], data["quantity"])
        totals += amount
    return totals

def calculate_total_quantity(datas) -> int:
    totals = 0
    for data in datas:
        totals += data["quantity"]
    return totals

