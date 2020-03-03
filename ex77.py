#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tups = ('macaco','geleia','laranja','igreja','leoa','leao marinho')
for palavra in tups:
    print (f'\nNa palavra {palavra} temos ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print (f'{letra}',end='')

