import sales_data

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
    calculate_difference_by_date
)

from sales_display import(
    show_sales,
    show_totals,
    show_totals_by_product,
    show_totals_by_date,
    show_product_ranking,
    show_compare_date
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


if __name__ == "__main__":
    datas = sales_data.sales_datas
    show_sales_action(datas)
    show_totals_action(datas)
    show_totals_by_product_action(datas)
    show_sorted_total_sales_ranking_by_product_action(datas)
    show_total_by_date_action(datas)
    show_compare_date_action(datas)



