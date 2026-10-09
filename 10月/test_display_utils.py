
from display_utils import (
    show_date_totals,
    show_average_minutes
)

def test_show_date_totals(capsys):
    #Arrange
    records = [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]
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

def test_show_average_minutes(capsys):
    #Arrange
    records = [
        {"date": "2026-10-06", "subject": "Python", "minutes": 90},
        {"date": "2026-10-07", "subject": "Python", "minutes": 120},
        {"date": "2026-10-07", "subject": "基本情報", "minutes": 60}
    ]
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

