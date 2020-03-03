"""Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""
lista = [[], [],[]]
for c in range (1,4):
    lista[0].append(int(input(f'Digite o {c} número da matriz: ')))
for d in range (4,7):
    lista[1].append(int(input(f'Digite o {d} número da matriz: ')))
for e in range (7,10):
    lista[2].append(int(input(f'Digite o {e} número da matriz: ')))
print (f'{lista[0]}\n{lista[1]}\n{lista[2]}')