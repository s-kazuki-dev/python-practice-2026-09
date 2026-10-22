import input_utils


def fake_input_date(message):
    if "開始日" in message:
        return "2026-10-06"
    return "2026-10-07"

def test_input_date_range(monkeypatch):
    monkeypatch.setattr(
        input_utils,
        "input_date",
        fake_input_date
    )
    result = input_utils.input_date_range()
    assert result == ("2026-10-06", "2026-10-07")


def fake_input_date_cancel_start(message):
    return None

def test_input_date_range_cancel_start(monkeypatch, capsys):
    monkeypatch.setattr(
        input_utils,
        "input_date",
        fake_input_date_cancel_start
    )
    result = input_utils.input_date_range()
    captured = capsys.readouterr()
    assert result is None
    assert "処理を中止しました" in captured.out


def fake_input_date_cancel_end(message):
    if "開始日" in message:
        return "2026-10-06"
    return None

def test_input_date_range_cancel_end(monkeypatch, capsys):
    monkeypatch.setattr(
        input_utils,
        "input_date",
        fake_input_date_cancel_end
    )
    result = input_utils.input_date_range()
    captured = capsys.readouterr()
    assert result is None
    assert "処理を中止しました" in captured.out


def fake_input_date_invalid_range(message):
    if "開始日" in message:
        return "2026-10-10"
    return "2026-10-05"

def test_input_date_range_invalid_range(monkeypatch, capsys):
    monkeypatch.setattr(
        input_utils,
        "input_date",
        fake_input_date_invalid_range
    )
    result = input_utils.input_date_range()
    captured = capsys.readouterr()
    assert result is None
    assert "開始日は終了日以前の日付を入力してください" in captured.out

def test_input_date_range_valid(monkeypatch):
    answers = ["2026-10-20","2026-10-22"]
    monkeypatch.setattr(
        input_utils,
        "input_date",
        lambda message: answers.pop(0)
    )
    result = input_utils.input_date_range()
    assert result == ("2026-10-20", "2026-10-22")

def test_input_date_range_same_date(monkeypatch):
    answers = ["2026-10-22", "2026-10-22"]
    monkeypatch.setattr(
        input_utils,
        "input_date",
        lambda message: answers.pop(0)
    )
    result = input_utils.input_date_range()
    assert result == ("2026-10-22", "2026-10-22")

def test_input_date_range_invalid_order(monkeypatch, capsys):
    answers =  ["2026-10-25", "2026-10-22"]
    monkeypatch.setattr(
        input_utils,
        "input_date",
        lambda message: answers.pop(0)
    )
    result = input_utils.input_date_range()
    captured = capsys.readouterr()
    assert result is None
    assert '開始日は終了日以前の日付を入力してください' in captured.out

