#Exercício Python 051:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))
decimo = primeiro + (9)*razao
for c in range (primeiro,decimo+razao,razao):
    print ('{}'.format(c), end = ' > ')
print ('FIM')