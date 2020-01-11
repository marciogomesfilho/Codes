#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
#O cálculo do IMC é feito dividindo o peso (em quilogramas) pela altura (em metros) ao quadrado. É simples calcular o seu IMC.
peso = float(input('Digite seu peso em KG: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
print ('Seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print ('Abaixo do peso, vai comer meu filho(a) :)')
    input()
elif imc >18.5 and imc < 25:
    print('Peso ideal, ta de boa, só manter')
    input()
    """"""
elif imc > 25 and imc < 30:
    print('Sobrepeso amigão bora fazer um regime!!')
    input()
elif imc > 30 and imc < 40:
    print('Obesidade, ta quase uma baleinha! rs')
    input()
elif imc > 40:
    print('OBESIDADE MORBIDA, SÓ ENTERRAR, MEUS PARABENS!!!')
    input()