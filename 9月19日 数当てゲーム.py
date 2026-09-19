import random

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def play_game():
    secret_number = random.randint(1, 100)
    history = []
    count = 0
    min_number = 1
    max_number = 100
    while True:
        user_number = input_integer(f'{min_number}～{max_number}の数字を当ててください')
        if user_number < min_number or user_number > max_number:
            print(f'{min_number}～{max_number}の数字で入力してください')
            continue
        count += 1
        history.append(user_number)
        if user_number == secret_number :
            print('正解です')
            print(f'{count}回で正解しました')
            break
        elif user_number < secret_number:
            print('もっと大きいです')
            min_number  = user_number + 1
        elif user_number > secret_number:
            print('もっと小さいです')
            max_number = user_number - 1
    print(f'予想履歴:{history}')

def run_game():
    while True:
        play_game()
        while True:
            play_continue = input('もう一度遊びますか？(y or n)')
            if play_continue == "y":
                break
            elif play_continue == "n":
                return
            else:
                print('yかnで入力してください')
        

run_game()
