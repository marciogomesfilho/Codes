#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""termo = int(input('Digite o 1 termo: '))
razao = int(input('Digite a razao: '))
decimo = termo + (razao*9)

for c in range(termo,decimo+ 1 ,razao):
    print ('{}'.format(c),end=' > ')
print ('FIM')"""

termo = int(input('Digite o 1 termo: '))
razao = int(input('Digite a razao:'))

cont = 1
while cont <=10:
    print ('{} > '.format(termo),end='')
    termo += razao
    cont +=1
print ('FIM')
