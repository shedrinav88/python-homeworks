def int_func(word_lower):
    return word_lower.capitalize()


my_list = input('Enter a sentence using lowercase words: ').split()
sentence = []
for word in my_list:
    new_word = int_func(word)
    sentence.append(new_word)
print(' '.join(sentence))
