def count_words(words):
    return len(words) 

def count_word_frequency(words):
    totals = {}
    for word in words:
        if word not in totals:
            totals[word] = 1
        else:
            totals[word] += 1
    return totals

def find_most_common_words(frequencies):
    max_words = []
    max_count = 0
    for word in frequencies:
        if frequencies[word] > max_count:
            max_count =frequencies[word]
    for word in frequencies:
        if frequencies[word] == max_count:
            max_words.append(word)
    return max_words, max_count

def clean_words(words):
    cleaned_words = []
    for word in words:
        clean_word = word.strip(".,!?")
        if clean_word:
            cleaned_words.append(clean_word)
    return cleaned_words

def count_unique_words(frequencies):
    return len(frequencies)

def find_longest_words(frequencies):
    longest_words = []
    max_length = 0
    for word in frequencies:
        if len(word) > max_length:
            max_length = len(word)
    for word in frequencies:
        if len(word) == max_length :
            longest_words.append(word)
    return longest_words, max_length

def calculate_average_word_length(words):
    total = 0
    for word in words:
        total += len(word)
    return total / len(words)

def sort_words_by_length(frequencies):
    sort_words = sorted(frequencies, key=lambda word:len(word), reverse=True)
    return sort_words

def show_text_report(text):
    words = text.lower().split()
    words = clean_words(words)
    if not words:
        print('文章が入力されていません')
        return
    word_count = count_words(words)
    frequencies = count_word_frequency(words)
    sorted_frequencies = sorted(frequencies.items(), key=lambda item:item[1], reverse=True)
    max_words, max_count = find_most_common_words(frequencies)
    unique_words_count = count_unique_words(frequencies)
    longest_words, max_length = find_longest_words(frequencies)
    average_length = calculate_average_word_length(words)
    sorted_words = sort_words_by_length(frequencies)

    print('-----文章分析-----')
    print(f'単語数:{word_count}')
    print(f'単語の種類数:{unique_words_count}')
    print('単語別出現回数')
    for word, count in sorted_frequencies:
        print(f'{word}:{count}回')
    print('最多単語')
    for word in max_words:
        print(f'{word}:{max_count}回')
    print('最長単語')
    for word in longest_words:
        print(f'{word}:{max_length}文字')
    print(f'平均単語長:{average_length}文字')
    print('文字数の長い順')
    for word in sorted_words:
        print(word)



text = input('文章を入力してください')
show_text_report(text)

