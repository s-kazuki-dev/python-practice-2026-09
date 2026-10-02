students = [
    {"name": "田中", "score": 78},
    {"name": "佐藤", "score": 92},
    {"name": "鈴木", "score": 65},
    {"name": "高橋", "score": 88},
    {"name": "伊藤", "score": 54}
]

def show_students(students):
    for student in students:
        print(f'{student["name"]}:{student["score"]}点')

def calculate_average_score(students):
    total = 0
    for student in students:
        total += student["score"]
    average = total / len(students)
    return average

def find_top_student(students):
    top_student = {}
    top_score = 0
    for student in students:
        if student["score"] > top_score:
            top_score = student["score"]
            top_student = student
    return top_student

def get_passed_students(students):
    passed_students = []
    for student in students:
        if student["score"] >= 60:
            passed_students.append(student)
    return passed_students

def sort_students_by_score(students):
    sorted_students =sorted(students, key=lambda student:student["score"], reverse=True)
    return sorted_students


show_students(students)

average = calculate_average_score(students)
print(f'平均点:{average}点')

top_student = find_top_student(students)
print(f'最高点:{top_student["name"]} {top_student["score"]}点')

passed_students = get_passed_students(students)
print('-----合格者-----')
show_students(passed_students)

sorted_students =sort_students_by_score(students)
print('-----点数ランキング-----')
show_students(sorted_students)


