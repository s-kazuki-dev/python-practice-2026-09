
from sales_data import (
    sales_datas
)

from sales_input import (
    input_integer,
    input_positive_integer,
    input_non_negative_integer,
    input_new_data,
    input_str
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
    calculate_difference_by_date,
    add_new_data,
    calculate_total_sales,
    calculate_total_quantity
    
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

#新データの登録と反映
def test_add_new_data():
    test_data = [{"date": "2026-10-26", "name": "コーヒー", "price": 400, "quantity": 2}]
    expected_data = [
        {"date": "2026-10-26", "name": "コーヒー", "price": 400, "quantity": 2},
        {"date":"2026-10-27", "name": "紅茶", "price": 300, "quantity": 2}
        ]
    expected_sales = 1400
    expected_quantity = 4
    result_data = add_new_data(test_data, "2026-10-27", "紅茶", 300, 2)
    result_sales = calculate_total_sales(result_data)
    result_quantity = calculate_total_quantity(result_data)
    assert result_data == expected_data
    assert test_data == expected_data
    assert result_sales == expected_sales
    assert result_quantity == expected_quantity


#input_strの入力テスト
def test_input_str_retry(monkeypatch):
    responses = iter(["", "       コーヒー"])
    monkeypatch.setattr(
        "builtins.input",
        lambda message: next(responses)
    )
    result = input_str("商品名を入力:")
    assert result == "コーヒー"

#input_integerの入力テスト
def test_input_integer(monkeypatch):
    responses = iter(["abc", "450"])
    monkeypatch.setattr(
        "builtins.input",
        lambda message: next(responses)
    )
    result = input_integer('数字を入力:')
    assert result == 450

#input_non_negative_integerの入力テスト
def test_input_non_negative(monkeypatch):
    responses = iter(["-100", "0"])
    monkeypatch.setattr(
        "builtins.input",
        lambda message: next(responses)
    )
    result = input_non_negative_integer('数字を入力:')
    assert result == 0

#input_positiveの入力テスト
def test_input_positive(monkeypatch):
    responses = iter(["0", "3"])
    monkeypatch.setattr(
        "builtins.input",
        lambda message: next(responses)
    )
    result = input_positive_integer('数字を入力:')
    assert result == 3

import sales_input
#input_new_dataの入力テスト
def test_input_new_data(monkeypatch):
    monkeypatch.setattr(
        sales_input,
        "input_str",
        lambda message: None
    )
    result = sales_input.input_new_data()
    assert result is None



