
import json

from pathlib import Path
folder = Path(__file__).resolve().parent
SALES_FILE = folder / "sales.json"

def load_sales():
    try:
        with open(SALES_FILE, "r", encoding="utf-8") as file:
            datas = json.load(file)
            return datas
    except FileNotFoundError:
        return []
    
def save_sales(datas):
    with open(SALES_FILE, "w", encoding="utf-8") as file:
        json.dump(datas, file, ensure_ascii=False, indent=2)


