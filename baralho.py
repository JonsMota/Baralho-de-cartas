import random

def gerar_baralho(n_copias=2, coringas=True, embaralhado=True):
    baralho = []

    naipes = list('♠♥♦♣')
    print(naipes)
    numeros = list('A23456789') + ['10'] + list('JQK')

    for naipe in naipes:
        for numero in numeros:
            carta = numero + naipe
            baralho.append(carta)
    if coringas:    
        baralho.extend(['JK1', 'JK2']) 
    
    if embaralhado:
        random.shuffle(baralho)

    return baralho

baralho = gerar_baralho()
print(baralho)