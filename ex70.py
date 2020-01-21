#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.#B) quantos produtos custam mais de R$1000.#C) qual é o nome do produto mais barato.
nome = ''
preco = 0
continuar = ''
total = 0
caros = 0
barato = ''
while True:
    nome = str(input('Digite o nome do produto: ')).lower().strip()
    preco = float(input('Digite o preço do produto (20.99): '))
    continuar = str(input('Deseja cadastrar mais? [S/N]: ')).strip().lower()
    total += preco
    if preco > 1000:
        caros += 1
    barato = nome
    if nome < barato:
        nome = barato
    if continuar in 'Nn':
        break
print (f'Total da compra: R$ {total}\nProdutos custando mais de R$1000.00: {caros}\nNome do produto mais barato: {barato}')
print ('Fim do programa')
