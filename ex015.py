#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.


km = float (input('digite quantos kms o carro rodou: '))
dias = float(input('digite por quantos dias o carro ficou alugado'))
valor = (60*dias) + (0.15*km)
print ('o valor ficou {}'.format(valor))
