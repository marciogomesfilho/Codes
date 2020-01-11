#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa
from math import hypot

oposto = float (input('digite o cateto oposto: '))
adja = float (input('digite o cateto adjacente: '))
print ('a hipotenusa é: ', hypot(oposto, adja))
