def vowel(user_word):
    v=('a','e','i','o','u')
    for i in v:
        if i in v:
            user_word=user_word.replace(i,'')
    print(user_word.upper())
    return user_word

user_word=input('enter any word ')
print(user_word.upper())
vowel(user_word)