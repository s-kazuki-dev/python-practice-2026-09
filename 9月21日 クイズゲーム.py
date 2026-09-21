import random
import json

def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as file:
            loaded_questions = json.load(file)
            return loaded_questions
    except FileNotFoundError:
        return []

def save_questions(questions):
    with open("questions.json", "w", encoding="utf-8") as file:
        json.dump(questions, file, ensure_ascii=False, indent=2)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください:')

def input_question(questions):
    while True:
        question_text = input('問題文を入力/中止と入力でキャンセル:').strip()
        if question_text == "中止":
            break
        answer = input('答えを入力/中止と入力でキャンセル:').strip()
        if answer == "中止":
            break
        if not question_text or not answer:
            print('問題文と答えを入力してください')
            continue
        add_question(questions, question_text, answer)
        print('問題を追加しました')
        break
        
def add_question(questions, question_text, answer):
    questions.append(
        {"question":question_text,"answer":answer}
    )
    save_questions(questions)

def run_quiz(questions):
    if not questions:
        print('問題がありません')
        return
    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)
    score = 0
    for question in quiz_questions:
        print(question["question"])
        user_answer = input('答えを入力:').strip()
        if user_answer == question["answer"]:
            print('正解')
            score += 1
        else:
            print('不正解')
            print(f'正解は{question["answer"]}です')
    print(f'{len(quiz_questions)}問中{score}問正解')
    if len(quiz_questions) == score:
        print('全問正解')
    elif len(quiz_questions) - 1 == score:
        print('惜しい')
    else:
        print('もう一度挑戦')

def show_questions(questions):
    if not questions:
        print('問題はありません')
        return
    for number,question in enumerate(questions,start=1):
        print(f'{number}.{question["question"]} / {question["answer"]}')

def delete_question(questions, question_number):
    if 1<= question_number <= len(questions):
        del questions[question_number-1]
        save_questions(questions)
        return True
    else:
        return False

def input_delete_question(questions):
    if not questions:
        print('問題がありません')
        return
    show_questions(questions)
    while True:
        delete_number = input_integer("削除番号を入力/0で中止:")
        if delete_number == 0:
            break
        if delete_question(questions, delete_number):
            print('削除しました')
            show_questions(questions)
            break
        else:
            print('正しい番号を入力してください:')
        

def main(questions):
    while True:
        print('-----------------')
        print('1.クイズを始める')
        print('2.問題を追加する')
        print('3.問題一覧を見る')
        print('4.問題を削除する')
        print('0.終了')
        print('-----------------')
        number = input_integer('番号を入力:')
        if number == 1:
            run_quiz(questions)
        elif number == 2:
            input_question(questions)
        elif number == 3:
            show_questions(questions)
        elif number == 4:
            input_delete_question(questions)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください:')

questions = load_questions()
main(questions)

