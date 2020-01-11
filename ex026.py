# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('digite a frase: ')).upper()

print('quantidade de letra A: {}'.format(frase.count('A')))
print('posicao do 1 a: {}'.format(frase.find('A')+1))
print('ultida posicao do 1 a : {}'.format(frase.rfind('A')+1))

