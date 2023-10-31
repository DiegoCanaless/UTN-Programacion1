def matches(word, letters, show_word):
    updated_word = list(show_word)
    for i in range(len(word)):
        if word[i] == letters:
            updated_word[i] = letters

    return updated_word

