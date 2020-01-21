#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    resp = str(input('Quer continuar? (S/N): ')).upper().strip()[0]
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print ('FIM DO PROGRAMA')
print ('Média: {}'.format(soma/cont))
print ('Maior: {}'.format(maior))
print ('Menor: {}'.format(menor))


