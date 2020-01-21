#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
# serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""print('='*100)
print ('{:^100}'.format('Banco24Horas'))
print('='*100)
saque = int(input('Digite quanto deseja sacar: R$'))
total = saque
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if ced == 50:
            ced == 20
        elif ced == 20:
            ced == 10
        elif ced == 10:
            ced == 1
            print (f'{totalced} notas de {ced}')
            break"""







"""cont1 = cont10 = cont20 = cont50 = 0
valor = int (input('Digite o valor: '))
cont50 = valor // 50
cont20 = valor // 20
cont10 = valor // 10
cont1 = valor // 1
print (cont50)
print(cont20)
print(cont10)
print(cont1)"""






"""print('=' * 30)
print(f'{"BANCO DO ANCAPISTÃO":^30}')
print(f'{"Máximo de R$ 10.000":^30}')
print('=' * 30)
saque = int(input('Valor do saque: R$ '))
lista = [50 , 20 , 10 , 1]
cont = 0
while True:
    if saque == 0:
        break
    else:
        valor = lista[cont]
        notas = saque // valor
        saque -= notas * lista[cont]
        cont += 1
        if notas == 1:
            mostrarnotas = str(f'{notas:2} nota de {valor} R$.')
            print(f'{mostrarnotas:>30}')
        if notas > 1:
            mostrarnotas = str(f'{notas:2} notas de {valor} R$.')
            print(f'{mostrarnotas:>30}')
print('FIM!')"""


while True:
    valor = int(input('Qual o valor deseja sacar? R$ '))
    valor50 = valor // 50
    valor20 = (valor % 50) // 20
    valor10 = ((valor % 50) % 20) // 10
    valor1 = (((valor % 50) % 20) % 10) // 1
    if valor50 > 0:
        print(f'{valor50} cédulas de R$ 50')
    if valor20 > 0:
        print(f'{valor20} cédulas de R$ 20')
    if valor10 > 0:
        print(f'{valor10} cédulas de R$ 10')
    if valor1 > 0:
        print(f'{valor1} cédulas de R$ 1')
    break
print('Volte sempre!!! Tenha um bom dia!')