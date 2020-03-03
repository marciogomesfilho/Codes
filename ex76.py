#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""tups = ('Banana',3,'Maca',5,'Pao',1, 'Carne', 10, 'Frango', 8)
print ('=-'*30)
print (f'{"LISTAGEM DE PREÇOS":^55}')
print ('=-'*30)

for pos in range (0,len(tups)):
    if pos % 2 == 0:
        print (f'{tups[pos]:.<30}', end='')
    else:
        print (f'R${tups[pos]:>2.2f}')"""




print ('-='*20)
print (f'{"MARCINHO STORE":^40}')
print ('-='*20)
produtos = ('Playstation 4',1900,'Iphone',1700,'Guitarra',500,'Play2',500,'Violao',400,'Livro',10,'TV',1600)
for pos in range (0,len(produtos)):
   if pos % 2 == 0:
       print (f'{produtos[pos]:.<30}',end='')
   else:
       print (f'R${produtos[pos]:.2f}')



