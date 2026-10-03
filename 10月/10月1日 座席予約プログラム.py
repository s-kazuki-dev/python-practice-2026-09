seats = [
    ["○", "○", "×", "○", "○"],
    ["×", "○", "○", "○", "×"],
    ["○", "×", "○", "○", "○"],
    ["○", "○", "×", "×", "○"]
]

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_seats(seats):
    print("  ",end="")
    for column_number in range(1,len(seats[0]) + 1):
        print(column_number, end=" ")
    print()
    row_number = 1
    for row in seats:
        print(row_number, end=" ")
        for seat in row:
            print(seat, end=" ")
        print()
        row_number += 1

def count_seats(seats):
    empty_count = 0
    reserved_count = 0
    for row in seats:
        for seat in row:
            if seat == "○":
                empty_count += 1
            elif seat == "×":
                reserved_count += 1
    return empty_count, reserved_count

def calculate_ratio(empty_count, reserved_count):
    total_count = empty_count + reserved_count
    empty_ratio = empty_count / total_count * 100 
    return empty_ratio

def judge_status(empty_ratio):
    if empty_ratio >= 50:
        return '空席に余裕があります'
    elif 20 <= empty_ratio < 50:
        return '残りわずかです'
    else:
        return 'ほぼ満席です'

def input_position(seats):
    while True:
        row = input_integer(f'行番号を入力してください(1～{len(seats)})/0で中止:')
        if row == 0:
            return
        elif 1 <= row <= len(seats):
            row -= 1
            break
        else:
            print('正しい番号を入力してください')
    while True:
        column = input_integer(f'列番号を入力してください(1～{len(seats[0])})/0で中止:')
        if column == 0:
            return
        elif 1 <= column <= len(seats[0]):
            column -= 1
            break
        else:
            print('正しい番号を入力してください')
    return row, column

def reserve_seat(seats):
    empty_count, _ = count_seats(seats)
    if empty_count == 0:
        return '空席がありません'
    position = input_position(seats)
    if position is None:
        return "予約を中止しました"
    else:
        row, column = position
    if seats[row][column] == "○":
        seats[row][column] = "×"
        return "予約しました"
    elif seats[row][column] == "×":
        return "すでに予約済みです"

def cancel_seat(seats):
    _, reserved_count = count_seats(seats)
    if reserved_count == 0:
        return '予約席がありません'
    position = input_position(seats)
    if position is None:
        return "予約キャンセルを中止しました"
    else:
        row, column = position
    if seats[row][column] == "×":
        seats[row][column] = "○"
        return "予約をキャンセルしました"
    else:
        return "元から空いています"

def show_menu():
    print('-----------')
    print('1.:予約する')
    print('2.:予約をキャンセルする')
    print('3.:座席状況を見る')
    print('4.:行ごとの空席数を見る')
    print('5.:全行の空席数を見る')
    print('0.:終了')
    print('-----------')

def show_status(seats):
    show_seats(seats)
    empty_count, reserved_count = count_seats(seats)
    empty_ratio = calculate_ratio(empty_count, reserved_count)
    status = judge_status(empty_ratio)
    print(f'空席:{empty_count}')
    print(f'予約済:{reserved_count}')
    print(f'空席率:{empty_ratio:.1f}%')
    print(status)

def count_empty_in_row(row):
    empty_count = 0
    for seat in row:
        if seat == "○":
            empty_count += 1
    return empty_count

def show_each_row(seats):
    while True:
        number = input_integer(f'確認する行番号を入力(1～{len(seats)})/0で中止')
        if number == 0:
            print('中止しました')
            return
        elif 1 <= number <= len(seats):
            empty_count = count_empty_in_row(seats[number-1])
            break
        else:
            print('正しい番号を入力してください')

    print(f'{number}行目の空席:{empty_count}席') 

def show_all_rows(seats):
    row_number = 1
    for row in seats:
        empty_count = count_empty_in_row(row)
        print(f'{row_number}行目の空席:{empty_count}席')
        row_number += 1
        
def run_menu(seats):
    while True:
        print('現在の座席表')
        show_seats(seats)
        show_menu()
        number = input_integer('番号を入力')
        if number == 0:
            print('終了します')
            break
        elif number == 1:
            message = reserve_seat(seats)
            print(message)
        elif number == 2:
            message = cancel_seat(seats) 
            print(message)
        elif number == 3:
            show_status(seats)
        elif number == 4:
            show_each_row(seats)
        elif number == 5:
            show_all_rows(seats)
        else:
            print('正しい番号を入力してください')


run_menu(seats)

