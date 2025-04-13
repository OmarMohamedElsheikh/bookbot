def count_words(text):
    words = text.split()
    return len(words)
def count_letters(text):
    letters = {}
    for i in text:
        if i.isalpha():
            i = i.lower() 
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters
