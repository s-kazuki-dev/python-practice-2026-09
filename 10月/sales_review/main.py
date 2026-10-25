import sales_data

from sales_process import(
    calculate_sales,
    calculate_total_sales,
    calculate_total_quantity
)

from sales_display import(
    show_sales,
    show_totals
)

def show_sales_action(datas):
    if not datas:
        print('記録がありません')
        return
    for data in datas:
        amount = calculate_sales(data["price"], data["quantity"])
        show_sales(data, amount)

def show_totals_action(datas):
    if not datas:
        print('記録がありません')
        return
    total_sales = calculate_total_sales(datas)
    total_quantity = calculate_total_quantity(datas)
    show_totals(total_sales, total_quantity)

datas = sales_data.sales_datas
show_sales_action(datas)
show_totals_action(datas)

