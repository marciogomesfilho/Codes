#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais
n1 = int (input('Digite o primeiro numero inteiro: '))
n2 = int(input('Digite o segundo numero inteiro: '))
if n1 > n2:
    print ('o primeiro valor digitado é maior')
elif n2 > n1:
    print ('o segundo valor digitado é maior')
elif n1 == n2:
    print ('não existe valor maior ou menor os dois sao iguais')
