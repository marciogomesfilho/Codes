#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

antigo = float(input('digite seu salário: '))
novo = antigo + (antigo*15/100)

print ('seu novo salário é de: {}'.format(novo))
