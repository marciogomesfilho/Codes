#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int (input('Digite um numero: '))
tot = 0
for c in range (1, n + 1 ):
    if n % c == 0:
        print ('\033[34m', end = ' ')
        tot +=1
    else:
        print ('\033[31m' , end = ' ')

    print ('{}'.format(c), end = ' ')
print ('\n\033[mO número {} foi dívisivel {} vezes'.format(n,tot))
if tot == 2:
    print ('\n NUMERO PRIMO')
else:
    print ('NUMERO NAO É PRIMO')