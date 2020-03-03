"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
numeros = list()
while True:
    numeros.append(int(input(f'Digite um numero: ')))
    opcao = str(input('Deseja continuar? [N/S] '))
    if opcao in 'Nn':
        break
quantidade = len(numeros)
print (f'Foram digitados {quantidade} números')
print ('Lista decrescente: ',end='')
numeros.sort(reverse=True)
print (numeros)
if 5 in numeros:
    print ('tem número 5')
else:
    print ('Não tem numero 5')