"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e
 o menor valor digitado e as suas respectivas posições na lista. """
valores = []
for bume in range (1,6):
    valores.append(int(input(f'Digite o {bume} valor: ')))
for p, c in enumerate(valores):
    print(f'Na posicao {p} encontrei o numero: {c} ')
valores.sort()
print (f'O maior valor é o: {(valores[-1])}')
print (f'O menor valor é o: {(valores[0])}')
