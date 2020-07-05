user_sentence = input('Enter a sentence: ')
a = user_sentence.split()
for word in range(len(a)):
    print(f'{word + 1}. {a[word]}') if len(a[word]) <= 10 else print(f'{word + 1}. {a[word][:10]}')
