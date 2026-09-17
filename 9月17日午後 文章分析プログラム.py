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

def find_most_common_word(frequencies):
    max_word = None
    max_count = 0
    for word in frequencies:
        if frequencies[word] > max_count:
            max_word = word
            max_count = frequencies[word]
    return max_word, max_count

def clean_words(words):
    cleaned_words = []
    for word in words:
        clean_word = word.strip(".,!?")
        if clean_word:
            cleaned_words.append(clean_word)
    return cleaned_words

def count_unique_words(frequencies):
    return len(frequencies)

def find_longest_word(words):
    longest_word = None
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word, max_length

def show_text_report(text):
    words = text.lower().split()
    words = clean_words(words)
    if not words:
        print('文章が入力されていません')
        return
    word_count = count_words(words)
    frequencies = count_word_frequency(words)
    sorted_frequencies = sorted(frequencies.items(), key=lambda item:item[1], reverse=True)
    max_word, max_count = find_most_common_word(frequencies)
    unique_words_count = count_unique_words(frequencies)
    longest_word, max_length = find_longest_word(words)

    print('-----文章分析-----')
    print(f'単語数:{word_count}')
    print(f'単語の種類数:{unique_words_count}')
    print('単語別出現回数')
    for word, count in sorted_frequencies:
        print(f'{word}:{count}回')
    print(f'最多単語:{max_word} {max_count}回')
    print(f'最長単語:{longest_word} {max_length}文字')



text = input('文章を入力してください')
show_text_report(text)

