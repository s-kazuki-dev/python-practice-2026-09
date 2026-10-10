
from display_utils import (
    show_date_totals,
    show_average_minutes,
    show_top_subject
)

def test_show_date_totals(sample_records,capsys):
    #Arrange
    records = sample_records
    #Act
    show_date_totals(records)
    captured = capsys.readouterr()
    #Assert
    assert "2026-10-06: 90分" in captured.out
    assert "2026-10-07: 180分" in captured.out

def test_show_date_totals_empty(capsys):
    #Arrange
    records = []
    #Act
    show_date_totals(records)
    captured = capsys.readouterr()
    #Assert
    assert "記録がありません" in captured.out

def test_show_average_minutes(sample_records,capsys):
    #Arrange
    records = sample_records
    #Act
    show_average_minutes(records)
    captured = capsys.readouterr()
    #Assert
    assert "平均学習時間: 90.0分" in captured.out

def test_show_average_minutes_empty(capsys):
    #Arrange
    records = []
    #Act
    show_average_minutes(records)
    captured = capsys.readouterr()
    #Assert
    assert "記録がありません" in captured.out

def test_show_top_subject(sample_records, capsys):
    show_top_subject(sample_records)
    captured = capsys.readouterr()
    assert "最も学習した科目: Python (210分)" in captured.out

def test_show_top_subject_empty(capsys):
    show_top_subject([])
    captured = capsys.readouterr()
    assert "記録がありません" in captured.out

