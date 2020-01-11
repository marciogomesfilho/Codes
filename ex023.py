# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('digite o número: '))


u = n // 1 % 10
d = n // 100 % 10
c = n // 100 % 10
m = n // 1000 % 10


print (u)
print (d)
print (c)
print (m)