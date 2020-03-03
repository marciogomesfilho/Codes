"""Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""
tups =   (int(input('Digite o valor 1: ')),
          int(input('Digite o valor 2: ')),
          int(input('Digite o valor 3: ')),
          int(input('Digite o valor 4: ')))
par = 0
print (f'Sua tupla é : {tups}')
print (f'O valor 9 apareceu {tups.count(9)} vezes')
if 3 in tups:
    print (f'O valor 1 valor 3 foi digitado na {tups.index(3)+1} posicao')
else:
    print ('o valor 3 nao foi digiado')
print ('Os valores pares digitados foram: ', end='')
for c in tups:
    if c % 2 == 0:
        print (c,end=' ')
    else:
        break
print ('Não houve valor par')



