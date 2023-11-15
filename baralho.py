import random
import os 

funcoes = {
    "0": "gerar baralho",
    "1": "mostrar baralho",
    "2": "dar as cartas aos jogadores",
    "3": "mostrar as cartas restante do baralho"
}

def gerar_baralho(n_copias=2, coringas=True, embaralhado=True):
    baralho = []

    naipes = list('♠♥♦♣')
    print(naipes)
    numeros = list('A23456789') + ['10'] + list('JQK')

    for _ in range(n_copias):
        for naipe in naipes:
            for numero in numeros:
                carta = numero + naipe
                baralho.append(carta)
        if coringas:    
            baralho.extend(['JK1', 'JK2']) 
    
    if embaralhado:
        random.shuffle(baralho)

    return baralho

def mostrar_baralho(baralho):
    print(f'Há {len(baralho)} cartas no baralho')
    print('Cartas:')
    print(' | '.join(baralho))

def dar_as_cartas(baralho, n_jogadores=4, n_cartas=5):
    jogadores = {} 

    for i in range(n_jogadores):
        mao = []
        while len(mao) < n_cartas:
            carta = baralho.pop(0)
            mao.append(carta)
        nome_jogador = f'Jogador {i+1}'
        jogadores[nome_jogador] = mao
    
    return jogadores

def mostrar_jogadores(jogadores):
    for jogador, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do jogador {jogador}')
        print('Cartas:')
        for carta in mao:
            print(f' -> {carta}')

while True:
    os.system("clear")
    print(funcoes)    
    print("O que deseja fazer?")
    op = int(input())
    
    os.system("clear")
    if op == 0:
        baralho = gerar_baralho()
    
    elif op == 1:
        mostrar_baralho(baralho)
       
    elif op == 2:
        jogadores = dar_as_cartas(baralho)
        mostrar_jogadores(jogadores)
    elif op == 3:
        mostrar_baralho(baralho)

    print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨") 
    print("0 - CONTINUAR | 9 - SAIR") 
    if input() == 9: 
        break 