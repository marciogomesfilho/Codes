# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
from random import randint
contadorvitoria = 0
while True:
    jogadorescolha = int(input('[ 1 ] Par \n[ 2 ] Ímpar \nEscolha: '))
    jogadornumero = int(input('Número: '))
    computadornumero = randint(1,11)
    print (f'O computador escolheu o número {computadornumero}')
    if (jogadornumero + computadornumero) % 2 == 0 and jogadorescolha == 1 or (jogadornumero + computadornumero) % 2 != 0 and jogadorescolha == 2:
        print('VOCÊ GANHOU!')
        contadorvitoria += 1
    else:
        print ('PC GANHOU!')
        break
print (f'Você ganhou {contadorvitoria} vezes consecutivas')
