
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

#日付ごとの売上と販売数量の表示
def show_totals_by_date(sales_by_date: dict[str, int], quantity_by_date: dict[str, int]) -> None:
    print('=====日別売上集計=====')
    for date in sales_by_date:
        print(f'[{date}]')
        print(f'販売数量: {quantity_by_date[date]}個')
        print(f'売上金額: {sales_by_date[date]}円')
    print('=====================')

#商品ごとの売上ランキング表示(同率順位あり)
def show_product_ranking(ranked_data: list[tuple[int, str, int]]) -> None:
    print('=====商品別売上ランキング=====')
    for rank, product, sales in ranked_data:
        spaces = 12 - len(product) * 2
        print(f'{rank}位 {product}{" " * spaces}{sales:>6}円')
    print('============================')

#日別売上比較
def show_compare_date(max_date: list[str], max_sales: int, min_date: list[str], min_sales: int, difference: int) -> None:
    print('=====日別売上比較=====')
    print(f'売上最高日: {",".join(max_date)}')
    print(f'売上金額:    {max_sales}円')
    print()
    print(f'売上最低日: {",".join(min_date)}')
    print(f'売上金額:   {min_sales}円')
    print()
    print(f'売上差額:   {difference}円')
    print('======================')

#メニュー表示
def show_run_menu():
    print('=====飲食店 売上管理システム=====')
    print('1.売上データを登録')
    print('2.売上集計を表示')
    print('0.終了')
    print('===============================')



