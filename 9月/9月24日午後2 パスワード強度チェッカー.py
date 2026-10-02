def eight_over(password):
    if len(password) >= 8:
        return "OK"
    else:
        return "NG"

def include_smallword(password):
    for character in password:
        if character.islower():
            return "OK"
    return "NG"

def include_bigword(password):
    for character in password:
        if character.isupper():
            return "OK"
    return "NG"

def include_number(password):
    for character in password:
        if character.isdigit():
            return "OK"
    return "NG"

def counts_ok(password):
    count = 0
    if eight_over(password) == "OK":
        count += 1
    if include_smallword(password) == "OK":
        count += 1
    if include_bigword(password) == "OK":
        count += 1
    if include_number(password) == "OK":
        count += 1
    return count

def judge_password(password):
    counts = counts_ok(password)
    if counts == 4:
        return "強い"
    elif counts == 3:
        return "普通"
    else:
        return "弱い"

def make_password():
    password = input('パスワードを入力:')

    print(f'8文字以上:{eight_over(password)}')
    print(f'小文字あり:{include_smallword(password)}')
    print(f'大文字あり:{include_bigword(password)}')
    print(f'数字あり:{include_number(password)}')
    print('-----------')
    print(f'強度:{judge_password(password)}')

make_password()

