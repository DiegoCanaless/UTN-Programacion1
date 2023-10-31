import random
from functions import *

list_words = ["computadora", "software", "hardware", "programacion", "algoritmo",
              "redes", "internet", "videojuegos", "interfaz", "desarrollo",
              "programador", "gestion", "nube", "robotica",
              "aplicacion", "sistema", "innovacion", "dispositivo",
              "tecnologia", "codigo"]

word_random = list_words[random.randint(0, 20)]
hidden_word = ["_" for _ in word_random]
attempts = 6

while attempts>0:
    print("Palabra: ", hidden_word)
    letter = input("Ingresa una letra: ").lower()


    if letter in word_random:
        hidden_word = matches(word_random, letter, hidden_word)
    else:
        print(("Letra Incorrecta"))
        attempts = attempts-1
        print(f'Intentos: {attempts}')

    if "".join(hidden_word) == word_random:
        print("GANASTE , la palabra a adivinar era: ", word_random)
        break
if attempts ==0:
        print("PERDISTE, la palabra a adivinar era: ", word_random)