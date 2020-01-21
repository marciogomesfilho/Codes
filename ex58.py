#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 1 e 3.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
contador = 0
print (' -- descubra que numero o computador pensou entre 1 e 3 -- ')
from random import randint
numero = (randint(1,4))
resposta = int( input('digite seu palpite: '))
while resposta != numero:
    contador = contador + 1
    resposta = int(input('Errou, tente novamente: '))
print ('ACERTOU!')
print ('Você errou {} vezes antes de acertar'.format(contador))
input()