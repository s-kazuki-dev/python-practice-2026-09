import json
from pathlib import Path

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

