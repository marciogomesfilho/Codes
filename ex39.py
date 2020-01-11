# Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoatt = date.today().year
ano = int(input('Digite o ano que você nasceu: '))
idade = anoatt - ano
var = idade - 18
var2 = var*-1
foiem = anoatt - var
vaiem = anoatt - var2
if idade == 18:
    print ('está na hora de se alistar!!!')
elif idade > 18:
    print ('já passaram {} anos desde seus 18 anos (alistamento)'.format(var))
    print ('seu alistamento foi em: {}'.format(foiem))
elif idade < 18:
    print ('Ainda não precisa se alistar, falta(m) {} para o alistamento'.format(var2))
    print ('seu alistamento será em: {}'.format(vaiem))