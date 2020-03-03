#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print ('Número adicionado')
    else:
        opcao = str(input('Numero repetido! Deseja continuar? [S/N]'))
        if opcao in 'Nn':
            break
numeros.sort()
print (f'Lista de numeros: {numeros}')