#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians

n = float (input('digite um número: '))
sin = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))

#COS TA CALCULANDO ERRADO N SEI PQ

print('o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}:  '.format(cos, tan, tan))




