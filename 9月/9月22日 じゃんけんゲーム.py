import random

hands = ["グー","チョキ","パー"]

def input_hand():
    while True:
        user_hand = input('グー or チョキ or パー を入力:')
        if user_hand == "グー" or user_hand == "チョキ" or user_hand == "パー":
            return user_hand
        else:
            print('グー・チョキ・パーで入力してください')

def show_each_hand(cpu_hand, user_hand):
    print(f'あなた:{user_hand}')
    print(f'コンピューター:{cpu_hand}')

def judge_result(user_hand, cpu_hand):
    if user_hand == cpu_hand:    
        return "draw"
        
    elif ((user_hand == "パー" and cpu_hand == "グー") 
            or (user_hand == "グー" and cpu_hand == "チョキ") 
            or (user_hand == "チョキ" and cpu_hand == "パー")
            ):
        return "win"
    else:
        return "lose"

def show_score(win_counts, lose_counts, draw_counts):
    print(f'{win_counts}勝 {lose_counts}敗 {draw_counts}分')

def play(hands):
    win_counts = 0
    lose_counts = 0
    draw_counts = 0
    while True:
        question = input('対戦しますか(y/n):').strip().lower()
        if question == "n":
            break

        elif not question == "y" and not question == "n":
            print('yかnで入力してください')
            continue

        elif question == "y":
            user_hand = input_hand()
            cpu_hand = random.choice(hands)
            show_each_hand(cpu_hand, user_hand)
            result = judge_result(user_hand,cpu_hand)
            if result == "draw":
                print('あいこです')
                draw_counts += 1
            elif result == "win":
                print('あなたの勝ちです')
                win_counts += 1
            elif result == "lose":
                print('あなたの負けです')
                lose_counts += 1

        print('現在の成績')
        show_score(win_counts,lose_counts,draw_counts)
       
    print('最終成績')
    show_score(win_counts,lose_counts,draw_counts)
    print('ゲームを終了します')

play(hands)
