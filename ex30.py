#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int (input('digite um numero inteiro: '))

if  numero / 2 % 0 == 0:
    print ('o numero é par')
else:
    print ('o numero é impar')