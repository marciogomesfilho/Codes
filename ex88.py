"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep
lista = list ()
temp = list ()
tot = 1
quantidade = int(input('Quantos joguinhos deseja fazer? '))
while tot <= quantidade:
    contador = 0
    while True:
        n = randint(1, 60)
        if n not in temp:
            temp.append(n)
            contador += 1
        if contador >= 6:
            break
    lista.append(temp[:])
    temp.clear()
    tot += 1
for num, jog in enumerate (lista):
    print (f'{num+1} JOGO ''>>>' f' {jog} ')
    sleep(1)
print ('<->'* 10)
print('BOA SORTE!!!')
print ('<->'* 10)
input()