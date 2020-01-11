#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
#que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois
l1 = float(input('Digite o primeiro lado do triangulo: '))
l2 = float(input('Digite o segundo lado do triangulo: '))
l3 = float(input('Digite o terceiro lado do triangulo: '))

if l1 < (l2+l3) and l2 < (l1+l3) and l3 < (l2+l1):
    print ('é um triângulo')
else:
    print ('Não é um triângulo')
if l1 == l2 and l2 == l3 and l1 == l3:
    print('Triangulo equilatero!')
elif l1 != l2 and l2 != l3 and l1 != l3:
    print ('Triangulo escaleno')
elif l1 == l3 and l2 != l3 and l2 != l1 or l2 == l3 and l1 != l2 and l1 != l3 or l2 == l1 and l3 != l1 and l3 != l2:
    print ('Triangulo isoseles')