# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

print (' -- descubra que numero o computador pensou entre 0 e 5 -- ')
from random import randint
numero = (randint(0,1))
resposta = int( input('digite seu palpite: '))
if resposta == numero:
    print ('você acertou!! parabéns')
else:
    print ('você errou')

input()



