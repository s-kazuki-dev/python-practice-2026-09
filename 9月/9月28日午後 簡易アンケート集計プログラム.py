answers = [
    {"name": "田中", "answer": "Python"},
    {"name": "佐藤", "answer": "JavaScript"},
    {"name": "鈴木", "answer": "Python"},
    {"name": "高橋", "answer": "SQL"},
    {"name": "伊藤", "answer": "Python"},
    {"name": "山田", "answer": "SQL"}
]

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_answers(answers):
    if not answers:
        print('記録がありません')
        return
    for answer in answers:
        print(f'{answer["name"]}:{answer["answer"]}')

def result_answers(answers):
    if not answers:
        print('記録がありません')
        return
    totals = {}
    for answer in answers:
        if answer["answer"] not in totals:
            totals[answer["answer"]] = 1
        else:
            totals[answer["answer"]] += 1
    for subject in totals:
        print(f'{subject}:{totals[subject]}票')

def ratio(answers):
    if not answers:
        print('記録がありません')
        return
    totals = {}
    for answer in answers:
        if answer["answer"] not in totals:
            totals[answer["answer"]] = 1
        else:
            totals[answer["answer"]] += 1
    for subject in totals:
        print(
            f'{subject}:{totals[subject] / len(answers) * 100 :.1f}%'
        )

def rank(answers):
    if not answers:
        print('記録がありません')
        return
    totals = {}
    for answer in answers:
        if answer["answer"] not in totals:
            totals[answer["answer"]] = 1
        else:
            totals[answer["answer"]] += 1
    sorted_answers = sorted(totals.items(), key=lambda item:item[1], reverse=True)
    for number, subject in enumerate(sorted_answers, start=1):
        print(f'{number}.{subject[0]} {subject[1]}票')

def top(answers):
    if not answers:
        print('記録がありません')
        return
    totals = {}
    for answer in answers:
        if answer["answer"] not in totals:
            totals[answer["answer"]] = 1
        else:
            totals[answer["answer"]] += 1
    sorted_answers = sorted(totals.items(), key=lambda item:item[1], reverse=True)
    print(f'トップは{sorted_answers[0][0]}:{sorted_answers[0][1]}票')

def add_answer(answers):
    while True:
        name = input('名前を入力:').strip()
        if not name:
            print('名前を入力してください')
        else:
            break
    while True:
        answer = input('回答を入力:').strip()
        if not answer:
            print('回答を入力してください')
        else:
            break
    answers.append({
        "name":name,
        "answer":answer
    })

def run_menu(answers):
    while True:
        print('-------------')
        print('1.回答一覧')
        print('2.集計')
        print('3.割合')
        print('4.ランキング')
        print('5.トップ')
        print('6.回答追加')
        print('0.終了')
        print('-------------')
        number = input_integer('番号を入力:')
        if number == 1:
            show_answers(answers)
        elif number == 2:
            result_answers(answers)
        elif number == 3:
            ratio(answers)
        elif number == 4:
            rank(answers)
        elif number == 5:
            top(answers)
        elif number == 6:
            add_answer(answers)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

run_menu(answers)
