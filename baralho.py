import random

def gerar_baralho(n_copias=2, coringas=True, embaralhado=True):
    baralho = []

    naipes = list('♠♥♦♣')
    print(naipes)
    numeros = list('A23456789') + ['10'] + list('JQK')

    for naipe in naipes:
        for numero in numeros:
            carta = numero + naipe
            print(carta)

gerar_baralho()
