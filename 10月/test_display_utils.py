
from record_types import Record

from display_utils import (
    show_date_totals,
    show_average_minutes,
    show_top_subject,
    show_records_by_date_range,
    show_date_range_total,
    show_date_range_average,
    show_date_range_summary,
    show_study_days,
    show_records,
    show_numbered_records,
    show_menu
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

def test_show_top_subject(capsys):
    show_top_subject("Python", 210)
    captured = capsys.readouterr()
    assert "最も学習した科目: Python (210分)" in captured.out

def test_show_records_by_date_range(sample_records, capsys):
    show_records_by_date_range(sample_records, "2026-10-07", "2026-10-07")
    captured = capsys.readouterr()
    assert "2026-10-07 Python 120分" in captured.out
    assert "2026-10-07 基本情報 60分" in captured.out

def test_show_records_by_date_range_no_match(sample_records, capsys):
    show_records_by_date_range(sample_records, "2026-10-08", "2026-10-10")
    captured = capsys.readouterr()
    assert "該当する記録がありません" in captured.out

def test_show_date_range_total(sample_records, capsys):
    show_date_range_total(sample_records, "2026-10-06", "2026-10-07")
    captured = capsys.readouterr()
    assert "期間内の合計学習時間: 270分" in captured.out


def test_show_date_range_total_no_match(sample_records, capsys):
    show_date_range_total(sample_records, "2026-10-08", "2026-10-10")
    captured = capsys.readouterr()
    assert "期間内の合計学習時間: 0分" in captured.out

def test_show_date_range_average(sample_records, capsys):
    show_date_range_average(sample_records, "2026-10-06", "2026-10-07")
    captured = capsys.readouterr()
    assert "期間内の平均学習時間: 90.0分" in captured.out

def test_show_date_range_average_no_match(sample_records, capsys):
    show_date_range_average(sample_records, "2026-10-08", "2026-10-10")
    captured = capsys.readouterr()
    assert "期間内の平均学習時間: 0分" in captured.out

def test_show_date_range_summary(sample_records, capsys):
    show_date_range_summary(sample_records, "2026-10-06", "2026-10-07")
    captured = capsys.readouterr()
    assert "期間内の学習サマリー" in captured.out
    assert "合計学習時間: 270分" in captured.out
    assert "平均学習時間: 90.0分" in captured.out
    assert "最も学習した科目: Python (210分)" in captured.out
    assert "学習日数: 2日" in captured.out

def test_show_date_range_summary_no_match(sample_records, capsys):
    show_date_range_summary(sample_records, "2026-10-08", "2026-10-10")
    captured = capsys.readouterr()
    assert "記録がありません" in captured.out

def test_show_study_days(sample_records, capsys):
    show_study_days(sample_records)
    captured = capsys.readouterr()
    assert "学習日数: 2日" in captured.out

def test_show_study_days_empty(capsys):
    show_study_days([])
    captured = capsys.readouterr()
    assert "学習日数: 0日" in captured.out

def test_show_records(capsys):
    records: list[Record] = [
        {"date": "2026-10-20", "subject": "Python", "minutes": 90}
    ]
    show_records(records)
    captured = capsys.readouterr()
    assert  captured.out == "日付:2026-10-20,科目:Python,学習時間:90分\n"

def test_show_records_empty(capsys):
    records: list[Record] = []
    show_records(records)
    captured = capsys.readouterr()
    assert captured.out == "記録がありません\n"

def test_show_numbered_records(capsys):
    records: list[Record] = [
        {"date": "2026-10-20", "subject": "Python", "minutes": 90},
        {"date": "2026-10-20", "subject": "SQL", "minutes": 60}
    ]
    show_numbered_records(records)
    captured = capsys.readouterr()
    assert captured.out == (
        "1.日付:2026-10-20,科目:Python,学習時間:90分\n"
        "2.日付:2026-10-20,科目:SQL,学習時間:60分\n"
    )

def test_show_numbered_records_empty(capsys):
    records: list[Record] = []
    show_numbered_records(records)
    captured = capsys.readouterr()
    assert captured.out == "記録がありません\n"

def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert "1.学習記録を見る" in captured.out
    assert "24.CSVに書き出す" in captured.out
    assert "0.終了" in captured.out

