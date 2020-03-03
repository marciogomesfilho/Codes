#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint
tups = (randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20))
print (tups)
print (min(tups))
print (max(tups))