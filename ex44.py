#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o preço do produto: '))
#a vista dinheiro/cheque
primeiro = produto - (produto*10)/100
# a vista no cartao
segundo = produto - (produto*5)/100
# em até 2x no cartao
terceiro = produto
# 3x ou mais no cartao
quarto = produto + (produto*20)/100


pagamento = str(input('digite a forma de pagamento (a,b,c ou d) e aperte enter: \n a: a vista dinheiro/cheque \n b: a vista no cartao \n c: em 2x no cartao \n d: 3x ou mais no cartao\n'))

if pagamento == 'a':
    print ('o Valor é: {}'.format(primeiro))
    input()
elif pagamento == 'b':
    print ('o Valor é: {}'.format(segundo))
    input()
elif pagamento == 'c':
    print('o Valor é: {}'.format(terceiro))
    input()
elif pagamento == 'd':
    print('o Valor é {}'.format(quarto))

    input()