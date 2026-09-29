seats = [
    ["○", "○", "○", "○"],
    ["○", "○", "○", "○"],
    ["○", "○", "○", "○"]
]

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_seats(seats):
    row_names = ["A", "B", "C"]
    print("   1  2  3  4")
    for i, row in enumerate(seats):
        print(row_names[i], end="  ")
        for seat in row:
            print(seat, end="  ")
        print()

def input_reserve():
    while True:
            row = input('行を入力/A or B or C/0でキャンセル:')
            if row == "0":
                return
            elif row not in ["A","B","C","0"]:
                print('正しい行を入力')
            else:
                if row == "A":
                    row = 0
                elif row == "B":
                    row = 1
                elif row == "C":
                    row = 2
                break
    while True:
        column = input_integer('列を入力/0でキャンセル:')
        if 1 <= column <= 4:
            column -= 1
            break
        elif column == 0:
            return
        else:
            print('正しい列を入力')
    return row, column
            
def reserve_seats(seats):
    yet, _ = count_seats(seats)
    if yet == 0 :
        print('全席埋まっています')
        return
    while True:
        result = input_reserve()
        if result is None:
            return
        row, column = result
        if seats[row][column] == "×":
            print('既に埋まっています')
        else:
            seats[row][column] = "×"
            print('予約しました')
            return

def cancel_seats(seats):
    _, already = count_seats(seats)
    if already == 0:
        print('全席空いています')
        return
    while True:
        result = input_reserve()
        if result is None:
            return
        row, column = result
        if seats[row][column] == "○":
            print('空いています')
        else:
            seats[row][column] = "○"
            print('キャンセルしました')
            return

def check_seats(seats):
    yet, already = count_seats(seats)
    print(f'空席数は{yet}席:予約席は{already}席')

def count_seats(seats):
    yet = 0
    already = 0
    for row in seats:
        for seat in row:
            if seat == "○":
                yet += 1
            else:
                already += 1
    return yet, already

def run_menu(seats):
    while True:
        print('------------')
        print('1.座席表を見る')
        print('2.座席を予約')
        print('3.予約をキャンセル')
        print('4.空席数を確認')
        print('0.終了')
        print('-------------')
        number = input_integer('番号を入力')
        if number == 1:
            show_seats(seats)
        elif number == 2:
            reserve_seats(seats)
        elif number == 3:
            cancel_seats(seats)
        elif number == 4:
            check_seats(seats)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')

run_menu(seats)

