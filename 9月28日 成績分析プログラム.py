students = [
    {"name": "田中", "scores": {"国語": 80, "数学": 70, "英語": 90}},
    {"name": "佐藤", "scores": {"国語": 65, "数学": 85, "英語": 75}},
    {"name": "鈴木", "scores": {"国語": 90, "数学": 60, "英語": 85}}
]

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_students(students):
    if not students:
        print('記録がありません')
        return
    for student in students:
        print(
            f'{student["name"]}: '
            f'国語{student["scores"]["国語"]}点 '
            f'数学{student["scores"]["数学"]}点 '
            f'英語{student["scores"]["英語"]}点 '
            )

def each_average(students):
    if not students:
        print('記録がありません')
        return
    for student in students:
        total = student["scores"]["国語"] + student["scores"]["数学"] + student["scores"]["英語"]
        average = total / len(student["scores"])
        print(f'{student["name"]}:{average:.1f}点')

def average_rank(students):
    if not students:
        print('記録がありません')
        return
    average_students = {}
    for student in students:
        total = student["scores"]["国語"] + student["scores"]["数学"] + student["scores"]["英語"]
        average = total / len(student["scores"])
        average_students[student["name"]] = average
    sorted_students = sorted(average_students.items(), key=lambda item:item[1], reverse=True)
    for sorted_student in sorted_students:
        print(f'{sorted_student[0]}:{sorted_student[1]:.1f}点')

def subject_average(students):
    if not students:
        print('記録がありません')
        return
    kokugo_total = 0
    sugaku_total = 0
    eigo_total = 0
    for student in students:
        kokugo_total += student["scores"]["国語"]
        sugaku_total += student["scores"]["数学"]
        eigo_total += student["scores"]["英語"]
    print(f'国語:{kokugo_total / len(students):.1f}点')
    print(f'数学:{sugaku_total / len(students):.1f}点')
    print(f'英語:{eigo_total / len(students):.1f}点')

def each_subject_top(students):
    if not students:
        print('記録がありません')
        return
    kokugo_name = None
    kokugo_top = 0
    sugaku_name = None
    sugaku_top = 0
    eigo_name = None
    eigo_top = 0
    for student in students:
        if student["scores"]["国語"] > kokugo_top:
            kokugo_top = student["scores"]["国語"]
            kokugo_name = student["name"]
        if student["scores"]["数学"] > sugaku_top:
            sugaku_top = student["scores"]["数学"]
            sugaku_name = student["name"]
        if student["scores"]["英語"] > eigo_top:
            eigo_top = student["scores"]["英語"]
            eigo_name = student["name"]
    print('科目別トップ')
    print(f'国語:{kokugo_name}:{kokugo_top}点')
    print(f'数学:{sugaku_name}:{sugaku_top}点')
    print(f'英語:{eigo_name}:{eigo_top}点')

def run_menu(students):
    if not students:
        print('記録がありません')
        return
    while True:
        print('-----------------')
        print('1.一覧')
        print('2.生徒別平均')
        print('3.平均点ランキング')
        print('4.科目別平均')
        print('5.科目別トップ')
        print('0.終了')
        print('------------------')
        number = input_integer('番号を入力:')
        if number == 1:
            show_students(students)
        elif number == 2:
            each_average(students)
        elif number == 3:
            average_rank(students)
        elif number == 4:
            subject_average(students)
        elif number == 5:
            each_subject_top(students)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

run_menu(students)
