# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:42:44 2022

@author: Dilshod
"""

import random as r
from uzwords import words


def random_word():
    word = r.choice(words)
    while "-" in word or " " in word:
        word = r.choice(words)
    return word.upper()


def consul_view(user_words, word):
    consul_letter = ""
    for letter in word:
        if letter in user_words:
            consul_letter += letter
        else:
            consul_letter += "-"
    return consul_letter


def play():
    word = random_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ""
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")

        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")         