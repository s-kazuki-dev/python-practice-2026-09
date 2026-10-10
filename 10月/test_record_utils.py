
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
    find_top_subject
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


    