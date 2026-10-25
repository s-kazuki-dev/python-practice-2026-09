def show_sales(data, amount) ->None:
    if not data:
        print('記録がありません')
        return
    print(f'{data["date"]} {data["name"]} 売上:{amount}円')

def show_totals(total_sales: int, total_quantity: int) -> None:
    print('=====全体の売上集計=====')
    print(f'総売上金額: {total_sales}円')
    print(f'総販売数量: {total_quantity}個')
    print('=======================')

