
from sales_data import (
    sales_datas
)

from sales_process import (
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

from sales_display import (
    show_totals_by_product,
    show_totals_by_date,
    show_product_ranking
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

#ランキングのテスト
def test_product_ranking():
    test_data = [
        {"date": "2026-10-20", "name": "コーヒー", "price": 400, "quantity": 1},
        {"date": "2026-10-20", "name": "カレー", "price": 900, "quantity": 1},
        {"date": "2026-10-20", "name": "ケーキ", "price": 800, "quantity": 1},
        {"date": "2026-10-21", "name": "コーヒー", "price": 400, "quantity": 1},
        {"date": "2026-10-21", "name": "カレー", "price": 900, "quantity": 1},
        {"date": "2026-10-21", "name": "紅茶", "price": 300, "quantity": 1}
    ]
    expected = [
        (1, "カレー", 1800),
        (2, "コーヒー", 800),
        (2, "ケーキ", 800),
        (4, "紅茶", 300)
    ]
    ranking = sorted_total_sales_ranking_by_product(test_data, reverse=True)
    ranked_data = add_competition_rank(ranking)
    assert ranked_data == expected

#日別売上集計
def test_calculate_by_date():
    test_data = [
        {"date": "2026-10-20", "name": "コーヒー", "price": 400, "quantity": 2},
        {"date": "2026-10-20", "name": "カレー", "price": 900, "quantity": 1},
        {"date": "2026-10-21", "name": "ケーキ", "price": 800, "quantity": 1},
        {"date": "2026-10-21", "name": "コーヒー", "price": 400, "quantity": 3},
        {"date": "2026-10-22", "name": "カレー", "price": 900, "quantity": 1},
        {"date": "2026-10-22", "name": "紅茶", "price": 300, "quantity": 3}
    ]
    expected_sales = {"2026-10-20": 1700, "2026-10-21": 2000, "2026-10-22": 1800}
    expected_quantity = {"2026-10-20": 3, "2026-10-21": 4, "2026-10-22": 4}
    result_sales = calculate_total_sales_by_date(test_data)
    result_quantity = calculate_total_quantity_by_date(test_data)
    assert result_sales == expected_sales
    assert result_quantity == expected_quantity

#日別売上比較
def test_daily_sales_comparison():
    test_data = [
            {"date": "2026-10-20", "name": "コーヒー", "price": 400, "quantity": 1},
            {"date": "2026-10-20", "name": "カレー", "price": 900, "quantity": 1},
            {"date": "2026-10-21", "name": "ケーキ", "price": 800, "quantity": 1},
            {"date": "2026-10-21", "name": "コーヒー", "price": 400, "quantity": 1},
            {"date": "2026-10-22", "name": "カレー", "price": 900, "quantity": 1},
            {"date": "2026-10-22", "name": "紅茶", "price": 300, "quantity": 1}
    ]
    expected_max = [
        ("2026-10-20", 1300)
    ]
    expected_min = [
        ("2026-10-21", 1200),
        ("2026-10-22", 1200)
    ]
    expected_difference = 100
    result_max = calculate_max_sales_date(test_data)
    result_min = calculate_min_sales_date(test_data)
    result_difference = calculate_difference_by_date(test_data)
    assert result_max == expected_max
    assert result_min == expected_min
    assert result_difference == expected_difference


