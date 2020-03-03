"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
 cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
 No final, mostre os valores pares e ímpares em ordem crescente."""
#1 forma de fazer
"""lista = list()
par = list()
impar = list()
for contador in range (1,8):
    n = (int(input(f'Digite o {contador} número: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print (lista)
print (par)
print (impar)"""

# 2 forma
# < impar > par
lista = [[],[]]
n = 0
for c in range (1,8):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        lista[1].append(n)
    else:
        lista[0].append(n)
lista[0].sort()
lista[1].sort()
print (f'Números pares: {lista[1]}')
print (f'Números impares: {lista[0]}')






