"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
lista = [[], [],[]]
par = []
maior = 0
for c in range (1,4):
    lista[0].append(int(input(f'Digite o {c} número da matriz: ')))
    if c % 2 == 0:
        par.append(c)
for d in range (4,7):
    lista[1].append(int(input(f'Digite o {d} número da matriz: ')))
    if d % 2 == 0:
        par.append(d)
for e in range (7,10):
    lista[2].append(int(input(f'Digite o {e} número da matriz: ')))
    if e % 2 == 0:
        par.append(e)
for loop in range (0,3):
    if loop == 0:
        maior = lista[1][loop]
    elif lista[1][loop] > maior:
        maior = lista[1][loop]
print (f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print (f'Soma de pares: {sum(par)}')
print (f'Soma dos valores da terceira coluna: {(lista[0][2] + lista[1][2] + lista[2][2])}')
print (f'O maior valor da segunda linha é: {maior}')