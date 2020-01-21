#Exercício Python 054:
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e
# quantas já são maiores

from datetime import date
atual = date.today().year
nova = 0
velha = 0
for pess in range (1,8):
    nasc = int ( input ('Digite o ano de nascimento da {} pessoa: '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        velha += 1
    else:
        nova += 1
print ('existem {} pessoas novas e {} pessoas velhas'.format(nova,velha))