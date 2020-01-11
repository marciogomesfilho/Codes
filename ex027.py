#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.


nome = str(input('digite seu nome completo: ')).strip()

nomes = nome.split()

print ('prazer em te conhecer')
print ('seu primeiro nome é: {}'.format(nomes[0]))
print ('seu ultimo nome é: {}'.format(nome[len(nomes)-1]))