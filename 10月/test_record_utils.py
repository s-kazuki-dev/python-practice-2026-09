
from record_types import Record

import pytest

from record_utils import(
    filter_records_by_subject,
    filter_records_by_date,
    calculate_total_minutes,
    calculate_subject_totals,
    calculate_average_minutes,
    calculate_date_total,
    calculate_date_totals,
    calculate_totals_by_key,
    find_top_subject,
    filter_records_by_date_range,
    calculate_date_range_total,
    calculate_date_range_average,
    calculate_date_range_summary
)

def create_test_records():
    return [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]

def test_filter_records_by_subject(sample_records):
    records = sample_records
    #Arrange
    subject = "Python"
    expected_count = 2
    #Act
    result = filter_records_by_subject(records,subject)
    #Assert
    assert len(result) == expected_count
    #Arrange
    subject = "Py"
    expected_count = 2
    #Act
    result = filter_records_by_subject(records,subject)
    #Assert
    assert len(result) == expected_count
    #Arrange
    subject = "SQL"
    expected = []
    #Act
    result = filter_records_by_subject(records,subject)
    #Assert
    assert result == expected

def test_filter_records_by_date(sample_records):
    records = sample_records
    #Arrange
    date = "2026-10-07"
    expected_count = 2
    #Act
    result = filter_records_by_date(records,date)
    #Assert
    assert len(result) == expected_count
    #Arrange
    date = "2026-10-08"
    expected = []
    #Act
    result = filter_records_by_date(records,date)
    #Assert
    assert result == expected

@pytest.mark.parametrize(
        "records, expected",
        [
        (
            [
                {"date": "2026-10-06", "subject": "Python", "minutes": 90},
                {"date": "2026-10-07", "subject": "Python", "minutes": 120},
                {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
            ],
            270
        ),
        ([], 0),
        (
            [{"date": "2026-10-06", "subject": "Python", "minutes": 90}],
            90
        )
        ]
    )
def test_calculate_total_minutes(records, expected):
    result = calculate_total_minutes(records)
    assert result == expected

def test_calculate_subject_totals(sample_records):
    records = sample_records
    #Arrange
    expected_python = 210
    expected_fe = 60
    #Act
    result = calculate_subject_totals(records)
    #Assert
    assert result["Python"] == expected_python
    assert result["基本情報"] == expected_fe
    #Arrange
    empty_records = []
    expected = {}
    #Act
    result = calculate_subject_totals(empty_records)
    #Assert
    assert result == expected

def test_records_are_independent():
    # Arrange
    records1 = create_test_records()
    records2 = create_test_records()

    # Act
    records1[0]["minutes"] = 999

    # Assert
    assert records2[0]["minutes"] == 90

@pytest.mark.parametrize(
        "records, expected",
        [
            ([
                {"date": "2026-10-06", "subject": "Python", "minutes": 90},
                {"date": "2026-10-07", "subject": "Python", "minutes": 120},
                {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
            ],
            90.0),
            ([], 0),
            ([{"date": "2026-10-07", "subject": "Python", "minutes": 120}],
             120.0)
        ]
)
def test_calculate_average_minutes(records, expected):
    result = calculate_average_minutes(records)
    assert result == expected

@pytest.mark.parametrize(
        "date, expected",
        [
            ("2026-10-06",90),
            ("2026-10-07",180),
            ("2026-10-08",0)
        ]
)
def test_calculate_date_total(sample_records, date, expected):
    result = calculate_date_total(sample_records, date)
    assert result == expected

def test_calculate_date_totals(sample_records):
    #Arrange
    records = sample_records
    expected = {
        "2026-10-06":90,
        "2026-10-07":180
    }
    #Act
    result = calculate_date_totals(records)
    #Assert
    assert result == expected
    #Arrange
    empty_records = []
    expected = {}
    #Act
    result = calculate_date_totals(empty_records)
    #Assert
    assert result == expected

def test_calculate_totals_by_key(sample_records):
    #Arrange
    records = sample_records
    key = "subject"
    expected = {
    "Python": 210,
    "基本情報": 60
    }
    #Act
    result = calculate_totals_by_key(records, key)
    #Assert
    assert result == expected
    #Arrange
    key = "date"
    expected = {
    "2026-10-06": 90,
    "2026-10-07": 180
    }
    #Act
    result = calculate_totals_by_key(records, key)
    #Assert
    assert result == expected

def test_find_top_subject(sample_records):
    result = find_top_subject(sample_records)
    assert result == ("Python", 210)

def test_find_top_subject_empty():
    result = find_top_subject([])
    expected = None
    assert result == expected

def test_filter_records_by_date_range(sample_records):
    records = sample_records
    start_date = "2026-10-06"
    end_date = "2026-10-07"
    expected = [
                {"date": "2026-10-06", "subject": "Python", "minutes": 90},
                {"date": "2026-10-07", "subject": "Python", "minutes": 120},
                {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
            ]
    result = filter_records_by_date_range(records, start_date, end_date)
    assert result == expected

def test_filter_records_by_date_range_empty():
    records = []
    start_date = "2026-10-06"
    end_date = "2026-10-07"
    expected = []
    result = filter_records_by_date_range(records, start_date, end_date)
    assert result == expected

def test_filter_records_by_date_range_excludes_outside(sample_records):
    records = sample_records
    start_date = "2026-10-07"
    end_date = "2026-10-07"
    expected = [
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]
    result = filter_records_by_date_range(records, start_date, end_date)
    assert result == expected

def test_filter_records_by_date_range_no_match(sample_records):
    records = sample_records
    start_date = "2026-10-08"
    end_date = "2026-10-10"
    expected = []
    result = filter_records_by_date_range(records, start_date, end_date)
    assert result == expected

def test_calculate_date_range_total(sample_records):
    records = sample_records
    start_date = "2026-10-06"
    end_date = "2026-10-07"
    expected = 270
    result = calculate_date_range_total(records, start_date, end_date)
    assert result == expected

def test_calculate_date_range_total_empty():
    records = []
    start_date = "2026-10-06"
    end_date = "2026-10-07"
    expected = 0
    result = calculate_date_range_total(records, start_date, end_date)
    assert result == expected

def test_calculate_date_range_average(sample_records):
    records = sample_records
    start_date = "2026-10-06"
    end_date = "2026-10-07"
    expected = 90.0
    result = calculate_date_range_average(records, start_date, end_date)
    assert result == expected

def test_calculate_date_range_average_no_match(sample_records):
    records = sample_records
    start_date = "2026-10-08"
    end_date = "2026-10-10"
    expected = 0
    result = calculate_date_range_average(records, start_date, end_date)
    assert result == expected

def test_find_top_subject_zero_minutes():
    records: list[Record] = [
    {"date": "2026-10-13", "subject": "Python", "minutes": 0}
    ]
    expected = ("Python", 0)
    result = find_top_subject(records)
    assert result == expected

def test_calculate_date_range_summary(sample_records):
    records = sample_records
    start_date = "2026-10-06"
    end_date = "2026-10-07"
    expected = {
        "total": 270,
        "average": 90.0,
        "top_subject": "Python",
        "top_minutes": 210
    }
    result = calculate_date_range_summary(records, start_date, end_date)
    assert result == expected

def test_calculate_date_range_summary_no_match(sample_records):
    records = sample_records
    start_date = "2026-10-08"
    end_date = "2026-10-10"
    result = calculate_date_range_summary(records, start_date, end_date)
    assert result is None

