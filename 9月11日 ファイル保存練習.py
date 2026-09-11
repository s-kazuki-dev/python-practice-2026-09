def save_study(add_study):
    with open("study.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{add_study}")

def load_study():
    try:    
        with open("study.txt", "r", encoding="utf-8") as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print('学習内容はまだありません')

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_study():
    text = load_study()
    if text is not None:
        print(text)

def run_study_manager():
    while True:
        print('1.学習内容を追加')
        print('2.学習内容を表示')
        print('0.終了')

        number = input_integer('番号を入力')
        if number == 1:
            add_study = input('追加する学習内容を入力')
            save_study(add_study)
        elif number == 2:
            show_study()
        elif number == 0:
            break
        else:
            print('正しい番号を入力')



run_study_manager()