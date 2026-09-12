import json

def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            loaded_tasks = json.load(file)
        return loaded_tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def add_task(tasks, task_name):
    tasks.append({
        "name":task_name,
        "done":False
    })
    save_tasks(tasks)

def delete_task(tasks, task_number):
    if 1<= task_number <= len(tasks):
        del tasks[task_number-1]
        save_tasks(tasks)
    else:
        print('正しい番号を入力してください')

def show_tasks(tasks):
    if not tasks:
        print('タスクはありません')
    else:
        for i in range(len(tasks)):
            if tasks[i]["done"]:
                print(f'{i+1}:{tasks[i]["name"]} [完了]')
            else:
                print(f'{i+1}:{tasks[i]["name"]} [未完了]')

def input_integer(message):
    while True:    
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def complete_task(tasks, task_number):
    if 1 <= task_number <= len(tasks):
        tasks[task_number-1]["done"] = True
        save_tasks(tasks)
    else:
        print('正しいタスク番号を入力してください')

def reset_tasks(tasks):
    answer = input('本当にすべて削除しますか？(yes or no)')
    if answer == "yes":
        tasks.clear()
        save_tasks(tasks)
    else:
        print('リセットをキャンセルしました')

def run_task_manager(tasks):
    while True:
        print('---------------------------------')
        print('1 →「タスク一覧」')
        print('2 → 「タスク追加」')
        print('3 → 「タスク削除」')
        print('4 → 「タスク完了」')
        print('5 → 「タスクリセット」')
        print('0 → 「終了します」')
        print('----------------------------------')
        number = input_integer('番号を入力')
        if number == 1:
            show_tasks(tasks)
        elif number == 2:
            task_name = input('タスク名を入力')
            add_task(tasks, task_name)
            show_tasks(tasks)
        elif number == 3:
            show_tasks(tasks)
            task_number = input_integer('番号を入力')
            delete_task(tasks, task_number)
            show_tasks(tasks)
        elif number == 4:
            show_tasks(tasks)
            task_number = input_integer('完了するタスク番号を入力')
            complete_task(tasks, task_number)
            show_tasks(tasks)
        elif number == 5:
            show_tasks(tasks)
            reset_tasks(tasks)
        elif number == 0:
            print('終了します')
            break
        else:
            print('正しい番号を入力してください')


tasks = load_tasks()
run_task_manager(tasks)