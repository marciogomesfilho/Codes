#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float (input('digite o preço do produto: '))
promo = preco - preco*5/100


print ('o produto na promocao sai por {}'.format (promo))