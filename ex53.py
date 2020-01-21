#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str (input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
reverso = ''
for letras in range (len(junto)-1, -1 ,-1):
    reverso += junto[letras]
print ('a frase {} ao inverso é {}'.format(junto,reverso))
if reverso == junto:
    print ('é paíndromo')
else:
    print ('não é')