#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos vai pagar a casa: '))
meses = anos*12
prestacao = casa/meses
salario2 = (salario*30)/100
if salario2 < prestacao:
    print ('Casa: {:.2f}\nSalario: {:.1f}\nAnos pagagando: {}\nMeses pagando: {}\nPrestação: {:.0f}\n30% do salário: {}\nEMPRÉSTIMO NEGADO'.format(casa,salario,anos, meses, prestacao,salario2))
elif salario2 > prestacao:
    print('EMRÉSTIMO APROVADO')
