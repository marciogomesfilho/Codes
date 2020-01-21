#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input('Digite o 1 termo: '))
razao = int(input('Digite a razao: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print ('{}'.format(termo),end=' > ')
        termo += razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos a mais deseja ver: '))
print ('Progressão finalizada com {} termos'.format(total))