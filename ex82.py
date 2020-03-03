#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numeros = list()
par = list()
impar = list()
while True:
    n = (int(input(f'Digite o número: ')))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break

print (f'Lista compelta: {numeros}')
numeros.sort()
print (f'Números em ordem: {numeros}')
numeros.sort(reverse=True)
print (f'Números em ordem decrescente: {numeros}')
print (f'Pares: {par}')
print (f'Impares: {impar}')