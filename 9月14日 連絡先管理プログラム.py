import json

def load_contacts():
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json","w", encoding= "utf-8") as file:
        json.dump(contacts, file, ensure_ascii = False, indent=2)

def input_integer(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print('数字で入力してください')

def show_contacts(contacts):
    if not contacts:
        print('連絡先はありません')
    else:
        for i in range(len(contacts)):
            print(f'{i+1}:{contacts[i]["name"]} {contacts[i]["tel_number"]}')

def add_contact(contacts, name, tel_number):
    contacts.append({
        "name":name,
        "tel_number":tel_number
    })
    save_contacts(contacts)

def input_contact(contacts):
    name = input("名前を入力:")
    tel_number = input('電話番号を入力:')
    add_contact(contacts,name,tel_number)
    show_contacts(contacts)

def find_contact(contacts, search_name):
    for contact in contacts:
        if contact["name"] == search_name:
            return contact
    return None

def search_contact(contacts):
    search_name = input('検索する名前を入力')
    search_list = find_contact(contacts, search_name)
    if search_list is not None:
        print(f'{search_list["name"]} {search_list["tel_number"]}')
    else:
        print('該当する連絡先がありません')

def delete_contact(contacts, contact_number):
    if 1 <= contact_number <= len(contacts):
        del contacts[contact_number - 1]
        save_contacts(contacts)
    else:
        print('正しい番号を入力してください')

def input_delete_contact(contacts):
    show_contacts(contacts)
    contact_number = input_integer('削除する番号を入力')
    delete_contact(contacts, contact_number)
    show_contacts(contacts)

def run_contact_manager(contacts):
    while True:
        print('---------------------------')
        print('1.連絡先一覧')
        print('2.連絡先追加')
        print('3.連絡先検索')
        print('4.連絡先削除')
        print('0.終了')
        print('---------------------------')
        number = input_integer('番号を入力')
        if number == 1:
            show_contacts(contacts)
        elif number == 2:
            input_contact(contacts)
        elif number == 3:
            search_contact(contacts)
        elif number == 4:
            input_delete_contact(contacts)
        elif number == 0:
            break
        else:
            print('正しい番号を入力してください')


contacts = load_contacts()
run_contact_manager(contacts)
