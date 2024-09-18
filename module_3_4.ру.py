def single_root_words(root_word, *other_words):
    root_word = root_word.lower()

    same_words = []

    for word in other_words:

        word_lower = word.lower()

        if root_word in word_lower or word_lower in root_word:
            same_words.append(word)  # Добавляем слово в список

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
