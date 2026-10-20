
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
    calculate_date_range_summary,
    count_study_days,
    convert_minutes_to_hours,
    has_subject,
    all_records_have_positive_minutes,
    find_first_record_by_subject,
    sort_records_by_minutes,
    sort_records_by_date_and_minutes,
    validate_minutes,
    create_record,
    normalize_subject
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
        "top_minutes": 210,
        "study_days": 2
    }
    result = calculate_date_range_summary(records, start_date, end_date)
    assert result == expected

def test_calculate_date_range_summary_no_match(sample_records):
    records = sample_records
    start_date = "2026-10-08"
    end_date = "2026-10-10"
    result = calculate_date_range_summary(records, start_date, end_date)
    assert result is None

def test_count_study_days(sample_records):
    records = sample_records
    expected = 2
    result = count_study_days(records)
    assert result == expected

def test_count_study_days_empty():
    records = []
    expected = 0
    result = count_study_days(records)
    assert result == expected

def test_convert_minutes_to_hours():
    totals = {
        "Python": 210,
        "基本情報": 60
    }
    expected = {
        "Python": 3.5,
        "基本情報": 1.0
    }
    result = convert_minutes_to_hours(totals)
    assert result == expected

def test_find_top_subject_tie():
    records: list[Record] = [
        {"date": "2026-10-16", "subject": "Python", "minutes": 60},
        {"date": "2026-10-16", "subject": "SQL", "minutes": 60}
    ]
    result = find_top_subject(records)
    assert result == ("Python", 60)

def test_has_subject_found(sample_records):
    result = has_subject(sample_records, "Python")
    assert result == True

def test_has_subject_not_found(sample_records):
    result = has_subject(sample_records, "SQL")
    assert result == False

def test_all_records_have_positive_minutes_true(sample_records):
    result = all_records_have_positive_minutes(sample_records)
    assert result is True

def test_all_records_have_positive_minutes_false():
    records: list[Record] = [
        {"date": "2026-10-16", "subject": "Python", "minutes": 60},
        {"date": "2026-10-16", "subject": "SQL", "minutes": 0}
    ]
    result = all_records_have_positive_minutes(records)
    assert result is False

def test_has_subject_empty():
    result = has_subject([], "Python")
    assert result is False

def test_all_records_have_positive_minutes_empty():
    result = all_records_have_positive_minutes([])
    assert result is True

def test_find_first_record_by_subject_found():
    records: list[Record] = [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]
    result = find_first_record_by_subject(records, "Python")
    assert result == {"date": "2026-10-06", "subject": "Python", "minutes": 90}

def test_find_first_record_by_subject_not_found():
    records: list[Record] = [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120}
    ]
    result = find_first_record_by_subject(records, "基本情報")
    assert result is None

def test_sort_records_by_minutes():
    records: list[Record] = [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]
    expected = [
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60},
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120}
    ]
    result = sort_records_by_minutes(records)
    assert result == expected

def test_sort_records_by_minutes_desc():
    records: list[Record] = [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
        ]
    expected = [
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
        ]
    result = sort_records_by_minutes(records, reverse=True)
    assert result == expected

def test_sort_records_by_date_and_minutes():
    records: list[Record] = [
        {"date": "2026-10-20", "subject": "Python", "minutes": 60},
        {"date": "2026-10-19", "subject": "SQL", "minutes": 120},
        {"date": "2026-10-19", "subject": "Python", "minutes": 90}
        ]
    expected = [
        {"date": "2026-10-19", "subject": "Python", "minutes": 90},
        {"date": "2026-10-19", "subject": "SQL", "minutes": 120},
        {"date": "2026-10-20", "subject": "Python", "minutes": 60}
        ]
    result = sort_records_by_date_and_minutes(records)
    assert result == expected


def test_sort_records_by_minutes_rejects_positional_reverse():
    records: list[Record] = [
    {"date": "2026-10-20", "subject": "Python", "minutes": 90}
    ]
    with pytest.raises(TypeError):
        sort_records_by_minutes(records, True) #type: ignore

def test_validate_minutes_valid():
    minutes = 60
    validate_minutes(minutes)

def test_validate_minutes_invalid():
    minutes = -10
    with pytest.raises(ValueError) as exc_info:
        validate_minutes(minutes)
    assert str(exc_info.value) == "学習時間は0以上にしてください"

def test_create_record_valid():
    expected = {
    "date": "2026-10-20",
    "subject": "Python",
    "minutes": 90
    }
    result = create_record("2026-10-20", "Python", 90)
    assert result == expected

def test_create_record_invalid_minutes():
    with pytest.raises(ValueError):
        create_record("2026-10-20", "Python", -10)

def test_create_record_invalid_subject():
    with pytest.raises(ValueError):
        create_record("2026-10-20", "", 90)

def test_create_record_subject_only_spaces():
    with pytest.raises(ValueError):
        create_record("2026-10-20", "   ", 90)

def test_create_record_invalid_date():
    with pytest.raises(ValueError):
        create_record("2026-13-40", "Python", 90)

def test_create_record_invalid_date_format():
    with pytest.raises(ValueError):
        create_record("2026-1-2", "Python", 90)

def test_create_record_normalizes_subject():
    expected = {
    "date": "2026-10-20",
    "subject": "Python",
    "minutes": 90
    }
    result = create_record("2026-10-20", "   Python   ", 90)
    assert result == expected

def test_normalize_subject():
    result = normalize_subject("   Python   ")
    assert result == "Python"

