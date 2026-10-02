tasks = [
    {"name":"pythonを勉強する", "done":False},
    {"name":"gitを復習する", "done":False}
]

def show_tasks(tasks):
    for i in range(len(tasks)):
        if not tasks[i]["done"]:
            print(f'{i+1}:{tasks[i]["name"]} [未完了]')
        else :
            print(f'{i+1}:{tasks[i]["name"]} [完了]')

def add_task(tasks, task_name):
    tasks.append({"name":task_name, "done":False})

def complete_task(tasks, task_number):    
    if 1 <= task_number <= len(tasks):
        tasks[task_number-1]["done"] = True
    else:
        print('正しいタスク番号を入力してください')  

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def run_task_manager(tasks):
    while True:
        print('1.タスク一覧 2.タスク追加 3.タスク完了 0.終了')
        user_input = input_integer('操作を選んでください:')
        if user_input == 1:
            show_tasks(tasks)
        elif user_input == 2:
            task_name = input('新しいタスクを入力してください')
            add_task(tasks, task_name)
            show_tasks(tasks)
        elif user_input == 3:
            task_number = input_integer('完了するタスク番号を入力してください')
            complete_task(tasks, task_number)
            show_tasks(tasks)
        elif user_input == 0:
            print('終了します')
            break
        else:
            print('正しい番号を入力してください')

run_task_manager(tasks)
