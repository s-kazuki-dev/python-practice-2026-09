
#記録ごとのの売上表示
def show_sales(data, amount) ->None:
    if not data:
        print('記録がありません')
        return
    print(f'{data["date"]} {data["name"]} 売上:{amount}円')

#全体の売上と販売数量の表示
def show_totals(total_sales: int, total_quantity: int) -> None:
    print('=====全体の売上集計=====')
    print(f'総売上金額: {total_sales}円')
    print(f'総販売数量: {total_quantity}個')
    print('=======================')

#商品ごとの売上と販売数量の表示
def show_totals_by_product(sales_by_product: dict[str, int], quantity_by_product: dict[str, int]) -> None:
    print('=====商品別売上集計=====')
    for product in sales_by_product:
        print(f'[{product}]')
        print(f'販売数量: {quantity_by_product[product]}個')
        print(f'売上金額: {sales_by_product[product]}円')
    print('=======================')


