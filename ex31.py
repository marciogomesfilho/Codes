#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('digite quantos kms foi a viagem: '))
if dist <= 200:
    print ('o valor da viagem foi: R${}'.format(dist*0.50))
else:
    print ('o valor da viagem foi: R${}'.format(dist*0.45))
