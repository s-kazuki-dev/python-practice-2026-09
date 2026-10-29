
from sales_input import (
    input_integer,
    input_new_data
)

from sales_process import(
    calculate_sales,
    calculate_total_sales,
    calculate_total_quantity,
    calculate_total_sales_by_product,
    calculate_total_quantity_by_product,
    sorted_total_sales_ranking_by_product,
    add_competition_rank,
    calculate_total_sales_by_date,
    calculate_total_quantity_by_date,
    calculate_max_sales_date,
    calculate_min_sales_date,
    calculate_difference_by_date,
    add_new_data
)

from sales_display import(
    show_sales,
    show_totals,
    show_totals_by_product,
    show_totals_by_date,
    show_product_ranking,
    show_compare_date,
    show_run_menu
)

from sales_storage import(
    load_sales,
    save_sales
)

#記録ごとの売上表示
def show_sales_action(datas):
    if not datas:
        print('記録がありません')
        return
    for data in datas:
        amount = calculate_sales(data["price"], data["quantity"])
        show_sales(data, amount)

#全体の売上と販売数量の表示
def show_totals_action(datas):
    if not datas:
        print('記録がありません')
        return
    total_sales = calculate_total_sales(datas)
    total_quantity = calculate_total_quantity(datas)
    show_totals(total_sales, total_quantity)

#商品ごとの売上と販売数量の表示
def show_totals_by_product_action(datas):
    if not datas:
        print('記録がありません')
        return
    sales_by_product = calculate_total_sales_by_product(datas)
    quantity_by_product =calculate_total_quantity_by_product(datas)
    show_totals_by_product(sales_by_product, quantity_by_product)

#日付ごとの売上と販売数量の表示
def show_total_by_date_action(datas):
    if not datas:
        print('記録がありません')
        return
    sales_by_date = calculate_total_sales_by_date(datas)
    quantity_by_date = calculate_total_quantity_by_date(datas)
    show_totals_by_date(sales_by_date, quantity_by_date)

#商品ごとの売上ランキング表示
def show_sorted_total_sales_ranking_by_product_action(datas):
    if not datas:
        print('記録がありません')
        return
    ranking = sorted_total_sales_ranking_by_product(datas, reverse=True)
    ranked_data = add_competition_rank(ranking)
    show_product_ranking(ranked_data)

#日別売上比較
def show_compare_date_action(datas):
    if not datas:
        print('記録がありません')
        return
    max_data = calculate_max_sales_date(datas)
    min_data = calculate_min_sales_date(datas)
    difference = calculate_difference_by_date(datas)
    max_date = []
    for data in max_data:
        max_date.append(data[0])
    max_sales = max_data[0][1]
    min_date = []
    for data in min_data:
        min_date.append(data[0])
    min_sales = min_data[0][1]
    show_compare_date(max_date, max_sales, min_date, min_sales, difference)

#売上データ登録
def show_add_new_data_action(datas):
    print('=====売上データ登録=====')
    new_data = input_new_data()
    if new_data is None:
        return
    date, product, price, quantity = new_data
    add_new_data(datas, date, product, price, quantity)
    save_sales(datas)
    print('売上データを登録しました')

#メニュー実行
def run_menu(datas):
    while True:
        show_run_menu()
        number = input_integer('番号を入力してください')
        if number == 1:
            show_add_new_data_action(datas)
        elif number == 2:
            show_totals_action(datas)
        elif number == 0:
            print('中止しました')
            return
        else:
            print('正しい番号を入力してください')
    

        

if __name__ == "__main__":
    datas = load_sales()
    show_sales_action(datas)
    show_totals_action(datas)
    show_totals_by_product_action(datas)
    show_sorted_total_sales_ranking_by_product_action(datas)
    show_total_by_date_action(datas)
    show_compare_date_action(datas)
    run_menu(datas)

