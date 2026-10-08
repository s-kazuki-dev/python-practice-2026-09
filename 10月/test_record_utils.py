
from record_utils import(
    filter_records_by_subject,
    filter_records_by_date,
    calculate_total_minutes,
    calculate_subject_totals,
    calculate_average_minutes,
    calculate_date_total
)

def create_test_records():
    return [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]

def test_filter_records_by_subject():
    records = create_test_records()
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

def test_filter_records_by_date():
    records = create_test_records()
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

def test_calculate_total_minutes():
    records = create_test_records()
    #Arrange
    expected = 270
    #Act
    result = calculate_total_minutes(records)
    #Assert
    assert result == expected
    #Arrange
    expected = 0
    #Act
    result = calculate_total_minutes([])
    #Assert
    assert result == expected

def test_calculate_subject_totals():
    records = create_test_records()
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

def test_calculate_average_minutes():
    #Arrange
    records = create_test_records()
    expected = 90
    #Act
    result = calculate_average_minutes(records)
    #Assert
    assert result == expected
    #Arrange 
    empty_records = []
    expected = 0
    #Act
    result =calculate_average_minutes(empty_records)
    #Assert
    assert result == expected

def test_calculate_date_total():
    #Arrange
    records = create_test_records()
    date = "2026-10-07"
    expected = 180
    #Act
    result = calculate_date_total(records, date)
    #Assert
    assert result == expected
    #Arrange
    date = "2026-10-08"
    expected = 0
    #Act
    result = calculate_date_total(records,date)
    #Assert
    assert result == expected

    