
import json


def load_sales():
    try:
        with open("sales.json", "r", encoding="utf-8") as file:
            datas = json.load(file)
            return datas
    except FileNotFoundError:
        return []
    
def save_sales(datas):
    with open("sales.json", "w", encoding="utf-8") as file:
        json.dump(datas, file, ensure_ascii=False, indent=2)

