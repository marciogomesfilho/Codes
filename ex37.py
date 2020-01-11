#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n1 = int(input('Digite o numero inteiro: '))
print ('''Conversão em:
1 - Binário
2 - Octal
3 - Hexadecimal''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print ('o número {} convertido em binário é: {}'.format(n1,bin(n1)[2:]))
elif opcao == 2:
    print ('o numero {} convertido em octal é: {}'.format(n1,oct(n1)[2:]))
elif opcao == 3:
    print ('o numero {} convertido em hexadecimal é {}'.format(n1,hex(n1)[2:]))
else:
    print ('opcao invalida, tente novamente')