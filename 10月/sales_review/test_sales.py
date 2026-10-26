from sales_process import (
    calculate_total_sales_by_product,
    calculate_total_quantity_by_product
    
)

from sales_display import (
    show_totals_by_product
)
#空データ/売上金額
def test_calculate_total_sales_by_product():
    test_data = []
    expected = {}
    result = calculate_total_sales_by_product(test_data)
    assert result == expected

#空データ/販売数量
def test_calculate_total_quantity_by_product():
    test_data = []
    expected = {}
    result = calculate_total_quantity_by_product(test_data)
    assert result == expected

#商品が１種類
def test_show_total_sales_by_product_one_type(capsys):
    test_data = [
        {"name": "コーヒー", "price": 400, "quantity": 5}
    ]
    sales_by_product = calculate_total_sales_by_product(test_data)
    quantity_by_product = calculate_total_quantity_by_product(test_data)
    show_totals_by_product(sales_by_product, quantity_by_product)
    captured = capsys.readouterr()
    assert ("[コーヒー]\n"
            "販売数量: 5個\n"
            "売上金額: 2000円\n"
    ) in captured.out

#同じ商品の価格が異なる
def test_show_total_sales_by_product_different_price(capsys):
    test_data = [
        {"name": "コーヒー", "price": 400, "quantity": 3},
        {"name": "コーヒー", "price": 500, "quantity": 2}
    ]
    sales_by_product = calculate_total_sales_by_product(test_data)
    quantity_by_product = calculate_total_quantity_by_product(test_data)
    show_totals_by_product(sales_by_product, quantity_by_product)
    captured = capsys.readouterr()
    assert ("[コーヒー]\n"
            "販売数量: 5個\n"
            "売上金額: 2200円\n"
    ) in captured.out

