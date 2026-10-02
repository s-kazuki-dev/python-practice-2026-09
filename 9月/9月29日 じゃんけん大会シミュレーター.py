import random

players = ["田中", "佐藤", "鈴木", "高橋"]

hands = ["グー", "チョキ", "パー"]

results = {}

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_players(players):
    print('---------------')
    for number, player in enumerate(players, start=1):
        print(f'{number}.{player}')
    print('---------------')

def choose_players(players):
    while True:
        one_player = input_integer('1人目を選択:')
        if 1 <= one_player <= len(players):
            break
        else:
            print('正しい番号を入力してください')
    while True:
        two_player = input_integer('2人目を選択:')
        if one_player == two_player:
            print('異なる人を選んでください')
        elif 1 <= two_player <= len(players):
            break
        else:
            print('正しい番号を入力してください')
    return one_player - 1, two_player - 1

def judge(one_hands, two_hands):
    if one_hands == two_hands:
        return "draw"
    elif ((one_hands == "グー" and two_hands == "チョキ") or
          (one_hands == "チョキ" and two_hands == "パー") or
          (one_hands == "パー" and two_hands == "グー")
          ):
        return "one_win"
    else:
        return "two_win"

def play_match(players, one, two):
    while True:
        one_hands = random.choice(hands)
        two_hands = random.choice(hands)
        print('-------------')
        print(f'{players[one]}:{one_hands}')
        print(f'{players[two]}:{two_hands}')
        print('-------------')
        result = judge(one_hands, two_hands)
        if result == "draw":
            print("あいこです")
        elif result == "one_win":
            print(f'{players[one]}の勝ち')
            return one
        elif result == "two_win":
            print(f'{players[two]}の勝ち')
            return two

def records_win_players(players, win_player):
    if players[win_player] not in results:
        results[players[win_player]] = 1
    else:
        results[players[win_player]] += 1
    
def run(players):
    while True:
        answer = input_integer('対戦しますか？/1 or 0:')
        if answer == 1:
            show_players(players)
            one, two = choose_players(players)
            win_player = play_match(players, one, two)
            records_win_players(players, win_player)
        elif answer == 0:
            break
        else:
            print('0か1で入力')
    print('最終成績')
    for name in players:
        if name in results:
            print(f'{name}:{results[name]}勝')
        else:
            print(f'{name}:0勝')

run(players)
