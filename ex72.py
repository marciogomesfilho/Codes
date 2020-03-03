#Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 5) e mostrá-lo por extenso.
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quarto', 'Cinco')
numero = int(input('Digite um número entre 0 e 5: '))
while numero not in range (0,6):
    numero = int(input('Tente novamente: '))
else:
    print(contagem[numero])














#lanche = ('Hamb', 'suco', 'pizza', 'pudim')

#for comida in lanche:
 #   print (f'eu vou comer {comida}')

#for cont in range (0,len(lanche)):
    #print (f'Comi {lanche[cont]}')
#for pos, comida in enumerate (lanche):
    #print (f'eu vou comer {comida} na posicao {pos}')
#print (sorted(lanche))
"""a = (2,5,4)
b = (5,8,1,2)
c = a + b
print (len(c))


print (c.count(5))

print(c.index(5,1))# o 1 depois, fala pra ele começar a procurar a partir do indx 1 desconsiderando o 0

pessoa = ('gustavo', 39, 'M', 99.88)
print (pessoa)


del (pessoa)
print (pessoa)"""