import json
from pathlib import Path

DATA_FILE = Path(__file__).parent/"books.json"

def load_books():
    try:
        with open("DATA_FILE", "r", encoding="utf-8") as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []

def save_books(books):
    with open("DATA_FILE","w",encoding="utf-8") as file:
        json.dump(books,file,ensure_ascii=False,indent=4)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_books(books):
    if not books:
        print('本がありません')
        return
    for number, book in enumerate(books,start=1):
        print(f'{number}.タイトル:{book["title"]},貸出可能:{book["stock"]}')

def input_book_number(books,message):
    while True:
        show_books(books)
        number = input_integer(message)
        if number == 0:
            return None
        elif 1 <= number <= len(books):
            return number
        else:
            print('正しい番号を入力してください')
    
def rent_book(books):
    if not books:
        print('本がありません')
        return
    while True:
        number = input_book_number(books,'借りる本番号を入力/0で中止:')
        if number is None:
            print('中止しました')
            return
        if books[number-1]["stock"] == "○":
            books[number-1]["stock"] = "×"
            print(f'{books[number-1]["title"]}を借りました')
            break
        else:
            print(f'{books[number-1]["title"]}は既に貸出中です')

def return_book(books):
    if not books:
        print('本がありません')
        return
    while True:
        number = input_book_number(books,'返す本番号を入力/0で中止:')
        if number is None:
            print('中止しました')
            return
        if books[number-1]["stock"] == "×":
            books[number-1]["stock"] = "○"
            print(f'{books[number-1]["title"]}を返しました')
            break
        else:
            print(f'{books[number-1]["title"]}は貸出中ではありません')
        
def show_loaned_books(books):
    if not books:
        print('本がありません')
        return
    loaned_books = []
    for book in books:
        if book["stock"] == "×":
            loaned_books.append(book)
    if not loaned_books:
        print('貸出中の本はありません')
    else:
        show_books(loaned_books)

def add_book(books):
    title = input('タイトル名を入力/0で中止:')
    if title == "0":
        return
    else:
        books.append(
            {"title":title, "stock":"○"}
        )
        print(f'{title}を追加しました')

def delete_book(books):
    if not books:
        print('本がありません')
        return
    number = input_book_number(books,'削除する本番号を入力/0で中止:')
    if number is None:
        print('中止しました')
        return
    del_title = books[number-1]["title"]
    del books[number-1]
    print(f'{del_title}を削除しました')

def show_loaned_status(books):
    if not books:
        print('本がありません')
        return
    available_count = 0
    loaned_count = 0
    for book in books:
        if book["stock"] == "○":
            available_count += 1
        else:
            loaned_count += 1
    total_count = available_count + loaned_count
    loaned_ratio = loaned_count / total_count * 100
    print(f'全冊数:{total_count}冊')
    print(f'貸出可能:{available_count}冊')
    print(f'貸出中:{loaned_count}冊')
    print(f'貸出率:{loaned_ratio:.1f}%')

def search_book(books):
    if not books:
        print('本がありません')
        return
    keyword = input('検索するタイトルを入力/0で中止:')
    found = False
    if keyword == "0":
        print('中止しました')
        return
    for book in books:
        if keyword in book["title"]:
            print(f'タイトル:{book["title"]},貸出可能:{book["stock"]}')
            found = True
    if found == False:
        print('見つかりませんでした')

def show_menu():
    print('-------------')
    print('1.:本一覧を見る')
    print('2.:本を借りる')
    print('3.:本を返す')
    print('4.:貸出中の本だけを見る')
    print('5.:本を追加する')
    print('6.:本を削除する')
    print('7.:貸出状況を見る')
    print('8.:タイトルから本を検索する')
    print('9.:データを保存する')
    print('0.:終了')
    print('--------------')

def run_menu(books):
    while True:
        show_menu()
        number = input_integer('番号を入力:')
        if number == 1:
            show_books(books)
        elif number == 2:
            rent_book(books)
        elif number == 3:
            return_book(books)
        elif number == 4:
            show_loaned_books(books)
        elif number == 5:
            add_book(books)
        elif number == 6:
            delete_book(books)
        elif number == 7:
            show_loaned_status(books)
        elif number == 8:
            search_book(books)
        elif number == 9:
            save_books(books)
            print('データを保存しました')
        elif number == 0:
            save_books(books)
            print('データを保存して終了します')
            break
        else:
            print('正しい番号を入力してください')

books = load_books()
run_menu(books)

