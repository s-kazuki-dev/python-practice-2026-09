
import storage_utils

def test_csv_round_trip(sample_records, tmp_path, monkeypatch):
    test_csv = tmp_path / "records.csv"
    monkeypatch.setattr(
        storage_utils,
        "CSV_FILE",
        test_csv
    )
    storage_utils.export_records_to_csv(sample_records)
    back = storage_utils.load_records_from_csv()
    assert sample_records == back

def test_load_records_from_csv_file_not_found(tmp_path, monkeypatch):
    missing_csv = tmp_path / "missing.csv"
    monkeypatch.setattr(
        storage_utils,
        "CSV_FILE",
        missing_csv
    )
    back = storage_utils.load_records_from_csv()
    assert back == []


