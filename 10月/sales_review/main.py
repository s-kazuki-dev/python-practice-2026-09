import sales_data

from sales_process import(
    calculate_sales,
    calculate_total_sales,
    calculate_total_quantity,
    calculate_total_sales_by_product,
    calculate_total_quantity_by_product
)

from sales_display import(
    show_sales,
    show_totals,
    show_totals_by_product
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

def show_totals_by_product_action(datas):
    if not datas:
        print('記録がありません')
        return
    sales_by_product = calculate_total_sales_by_product(datas)
    quantity_by_product =calculate_total_quantity_by_product(datas)
    show_totals_by_product(sales_by_product, quantity_by_product)


if __name__ == "__main__":
    datas = sales_data.sales_datas
    show_sales_action(datas)
    show_totals_action(datas)
    show_totals_by_product_action(datas)


