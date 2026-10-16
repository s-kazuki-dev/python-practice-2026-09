
import csv
import json
from pathlib import Path
from record_types import Record

CSV_FILE = Path(__file__).parent / "records.csv"
DATA_FILE = Path(__file__).parent / "records_with_date.json"


def load_records():
    try:
        with open(DATA_FILE,"r",encoding="utf-8") as file:
            records = json.load(file)
            return records
    except FileNotFoundError:
        return []

def save_records(records):
    with open(DATA_FILE,"w",encoding="utf-8") as file:
        json.dump(records,file,ensure_ascii=False,indent=4)

def export_records_to_csv(records: list[Record]) -> None:
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["date", "subject", "minutes"]
        )
        for record in records:
            writer.writerow(
                [record["date"], record["subject"], record["minutes"]]
            )

def load_records_from_csv() -> list[Record]:
    try:
        with open(CSV_FILE, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            records: list[Record] = []
            for row in reader:
                record: Record = {
                    "date": row["date"],
                    "subject": row["subject"],
                    "minutes": int(row["minutes"])
                }
                records.append(record)
            return records
    except FileNotFoundError:
        return []
            
