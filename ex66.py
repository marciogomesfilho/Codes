#Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
n = 0
contsoma = 0
contvezes = 0
while True:
    n = int(input('Digite o(s) número(s)[999 PARA]: '))
    if n == 999:
        break
    contsoma += n
    contvezes += 1
print (f'Foram digitados {contvezes} números e a soma deles é: {contsoma}')
print ('Fim do programa')