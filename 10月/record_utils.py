#科目ごとの絞り込み
def filter_records_by_subject(records,keyword):
    filtered_records = []
    for record in records:
        if keyword in record["subject"]:
            filtered_records.append(record)
    return filtered_records

#日付ごとの絞り込み
def filter_records_by_date(records,date):
    filtered_records = []
    for record in records:
        if record["date"] == date:
            filtered_records.append(record)
    return filtered_records

#合計学習時間
def calculate_total_minutes(records):
    total = 0
    for record in records:
        total += record["minutes"]
    return total

#合計学習時間(科目ごと)
def calculate_subject_totals(records):
    return calculate_totals_by_key(records, "subject")

def calculate_average_minutes(records):
    if not records:
        return 0
    total = calculate_total_minutes(records)
    average = total / len(records)
    return average

def calculate_date_total(records, date):
    filtered_records = filter_records_by_date(records, date)
    total = calculate_total_minutes(filtered_records)
    return total

def calculate_date_totals(records):
    return calculate_totals_by_key(records, "date")
    
def calculate_totals_by_key(records, key):
    totals = {}
    for record in records:
        if record[key] not in totals:
            totals[record[key]] = record["minutes"]
        else:
            totals[record[key]] += record["minutes"]
    return totals

def find_top_subject(records):
    if not records:
        return None
    result = calculate_subject_totals(records)
    max_minutes = 0
    max_subject = None
    for subject, minutes in result.items():
        if minutes > max_minutes:
            max_minutes = minutes
            max_subject = subject
    return (max_subject, max_minutes)

