#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = c = c2 = 0
n = int(input('Digite o número: '))

while n != 999:
    c += n
    c2 += 1
    n = int(input('Digite um número: '))

print ('Foram digitados {} números e a soma deles é {}'.format(c2, c))


print ('Fim do programa')