# Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#import math

#n = float (input('digite um numero: '))
#print ('o número digitado foi o {} e seu inteiro é o {}'.format(n, math.trunc(n)))

#*********************

from math import trunc

n = float (input('digite o numero: '))
print ('o numero digitado foi o {} e seu valor real é o {}'.format(n, trunc(n)))

