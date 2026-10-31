from channel_review import (
    total_sales_and_quantity,
    total_sales_and_quantity_by_channel,
    sales_ranking_by_channel,
    add_competition
)


sample_datas = [
    {"date": "2026-10-30", "channel": "テイクアウト", "name": "ケーキ", "price": 500, "quantity": 4},
    {"date": "2026-10-31", "channel": "デリバリー", "name": "コーヒー", "price": 450, "quantity": 2}
]

def test_total_sales_and_quantity():
    result = total_sales_and_quantity(sample_datas)
    empty_result = total_sales_and_quantity([])
    assert result == (2900, 6)
    assert empty_result == (0,0)

def test_total_sales_and_quantity_by_channel():
    result = total_sales_and_quantity_by_channel(sample_datas)
    empty_result = total_sales_and_quantity_by_channel([])
    total_sales, total_quantity = result
    assert total_sales == {"テイクアウト": 2000, "デリバリー": 900}
    assert total_quantity == {"テイクアウト": 4, "デリバリー": 2}
    assert empty_result == ({}, {})

def test_sales_ranking_by_channel():
    result = sales_ranking_by_channel(sample_datas)
    empty_result = sales_ranking_by_channel([])
    assert result == [("テイクアウト", 2000), ("デリバリー", 900)]
    assert empty_result == []

def test_sales_ranking_by_channel_empty():
    empty_data = []
    result = sales_ranking_by_channel(empty_data)
    assert result == []

def test_add_competition():
    test_datas = [
        {"date": "2026-10-30", "channel": "テイクアウト", "name": "ケーキ", "price": 500, "quantity": 4},
        {"date": "2026-10-31", "channel": "デリバリー", "name": "コーヒー", "price": 450, "quantity": 2},
        {"date": "2026-10-31", "channel": "店内", "name": "紅茶", "price": 400, "quantity": 5}
    ]
    empty_datas = []
    result = add_competition(test_datas)
    empty_result = add_competition(empty_datas)
    assert result == [
        (1, "テイクアウト", 2000),
        (1, "店内", 2000),
        (3, "デリバリー", 900)
    ]
    assert empty_result == []


