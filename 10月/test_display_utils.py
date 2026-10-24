
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
    show_menu,
    show_total_minutes, 
    show_subject_totals,
    show_selected_subject_total,
    show_date_total,
    show_date_subject_totals,
    show_date_range_label_ranking_header,
    show_label_ranking,
    show_selected_subject_ranking_by_date_header
   
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
    assert "23.CSVに書き出す" in captured.out
    assert "24.期間内の科目別ランキングを見る" in captured.out
    assert "25.日別合計学習時間ランキングを見る" in captured.out
    assert "28.指定した期間内で指定した科目の日別学習時間ランキングを見る" in captured.out
    assert "0.終了" in captured.out

def test_show_total_minutes(capsys):
    show_total_minutes(210)
    captured = capsys.readouterr()
    assert captured.out == "合計学習時間:210分\n"

def test_show_subject_totals(capsys):
    totals: dict[str, int] ={"Python": 210, "SQL": 60}
    show_subject_totals(totals)
    captured = capsys.readouterr()
    assert captured.out == (
        "科目別合計学習時間\n"
        "Python:210分\n"
        "SQL:60分\n"
    )

def test_show_selected_subject_total(capsys):
    show_selected_subject_total("Python", 210)
    captured = capsys.readouterr()
    assert captured.out == "Pythonの合計学習時間:210分\n"

def test_show_date_total(capsys):
    show_date_total("2026-10-21", 90)
    captured = capsys.readouterr()
    assert captured.out == "2026-10-21の合計学習時間:90分\n"

def test_show_date_subject_totals(capsys):
    totals: dict[str, int] = {"Python": 90, "SQL": 60}
    date = "2026-10-21"
    show_date_subject_totals(date, totals)
    captured = capsys.readouterr()
    assert captured.out == (
        "2026-10-21の科目別学習時間\n"
        "Python:90分\n"
        "SQL:60分\n"
    )

def test_show_subject_ranking(capsys):
    ranking: list[tuple[int, str, int]] = [
        (1, "Python", 210),
        (2, "基本情報", 60),
        (2, "SQL", 60),
        (4,"簿記", 30)
    ]
    show_label_ranking(ranking)
    captured = capsys.readouterr()
    assert captured.out == (
        "1位 Python: 210分\n"
        "2位 基本情報: 60分\n"
        "2位 SQL: 60分\n"
        "4位 簿記: 30分\n"
    )

def test_show_date_range_label_ranking_header_subject(capsys):
    show_date_range_label_ranking_header("2026-10-01", "2026-10-22", "科目")
    captured = capsys.readouterr()
    assert captured.out == "2026-10-01 ～ 2026-10-22 の科目別ランキング\n"

def test_show_date_range_label_ranking_header_date(capsys):
    show_date_range_label_ranking_header("2026-10-01", "2026-10-22", "日付")
    captured = capsys.readouterr()
    assert captured.out == "2026-10-01 ～ 2026-10-22 の日付別ランキング\n"

def test_show_date_ranking(capsys):
    ranking: list[tuple[int, str, int]] = [
            (1, "2026-10-22", 210),
            (2, "2026-10-20", 120),
            (2, "2026-10-21", 120),
            (4, "2026-10-19", 90)
        ]
    show_label_ranking(ranking)
    captured = capsys.readouterr()
    assert captured.out == (
        "1位 2026-10-22: 210分\n"
        "2位 2026-10-20: 120分\n"
        "2位 2026-10-21: 120分\n"
        "4位 2026-10-19: 90分\n"
    )

def test_show_selected_subject_ranking_by_date_header(capsys):
    show_selected_subject_ranking_by_date_header("Python")
    captured = capsys.readouterr()
    assert captured.out == "Pythonの日別学習時間ランキング\n"

