"""Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print ("""
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma é: {} '.format(soma))
    elif opcao == 2:
        mult = n1*n2
        print('Resultado: {}'.format(mult))
    elif opcao == 3:
        if n1 == n2:
            print ('mesmo valor')
        elif n1 > n2:
            maior = n1
            print ('maior valor é: {}'.format(n1))
        elif n2 > n1:
            maior = n2
            print ('Entre {} e {} o maior valor é o {}'.format(n1,n2,maior))
    elif opcao == 4:
        print ('Informe os números novamente: ')
        n1 = int(input('Digite o 1 numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print ('finalizando ',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print('.',end='')
        sleep(1)
        print ('.',end='')
        sleep(1)
        print('.', end='')
    else:
        print ('opção invalida')
sleep(1)
print ('fim do programa')
input()