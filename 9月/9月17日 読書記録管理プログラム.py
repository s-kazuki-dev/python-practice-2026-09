import json

def load_books():
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            books = json.load(file)
            return books
    except FileNotFoundError:
        return []

def save_books(books):
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=2)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def input_rating(message):
    while True:
        number = input_integer(message)
        if 1 <= number <= 5:
            return number
        else:
            print('1～5で入力してください')

def show_books(books):
    if not books:
        print('本が登録されていません')
        return
    for number, book in enumerate(books, start=1):
        print(f'{number}.{book["title"]}/{book["author"]}/評価:{book["rating"]}')

def search_books(books, keyword):
    results = []
    for book in books:
        if keyword in book["title"]:
            results.append(book)
    return results

def add_book(books, title, author, rating):
    books.append({
        "title":title,
        "author":author,
        "rating":rating
    })

def input_add_book(books):
    title = input('タイトルを入力')
    author = input('著者を入力')
    rating = input_rating('評価を入力')
    add_book(books, title, author, rating)
    save_books(books)
    print('本を追加しました')

def update_rating(books, book_number, new_rating):
    if 1 <= book_number <= len(books):
        update_book = books[book_number-1]
        update_book["rating"] = new_rating
        return True
    else:
        print('正しい番号を入力してください')
        return False

def input_update_rating(books):
    show_books(books)
    book_number = input_integer('変更したい本の番号を入力')
    if not 1 <= book_number <= len(books):
        print('正しい番号を入力してください')
        return
    new_rating = input_rating('新しい評価を1～5で入力')
    if update_rating(books, book_number, new_rating):
        save_books(books)
        print('評価を変更しました')
    
def delete_book(books, book_number):
    if 1 <= book_number <= len(books):
        del books[book_number-1]
        return True
    else:
        print('正しい番号を入力してください')
        return False

def input_delete_book(books):
    show_books(books)
    number = input_integer('削除する本の番号を入力')
    if delete_book(books, number):
        save_books(books)
        print('削除しました')

def run_book_manager(books):
    while True:
        print('-----読書記録管理-----')
        print('1.本の一覧')
        print('2.本を検索')
        print('3.本を追加')
        print('4.評価を変更')
        print('5.本を削除')
        print('0.終了')
        number = input_integer('番号を入力')
        if number == 1:
            show_books(books)
        elif number == 2:
            keyword = input('キーワード入力')
            results = search_books(books, keyword)
            show_books(results)
        elif number == 3:
            input_add_book(books)
        elif number == 4:
            input_update_rating(books)
        elif number == 5:
            input_delete_book(books)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')



books = load_books()
run_book_manager(books)


