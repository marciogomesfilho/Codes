#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
contaidade = 0
contmulher = 0
homemvelho = 0
nomevelho = 0
for c in range (1,5):
    print ('*** {} PESSOA ***'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = input( 'Sexo(M/F): ').upper()
    contaidade += idade
    media = contaidade/4
    if sexo == 'F' and idade < 20:
        contmulher += 1
    if c == 1 and sexo == 'M':
        homemvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
print ('O grupo possui {} mulher(es) com menos de 20 anos'.format(contmulher))
print ('A média da idade do grupo é {}'.format(media))
print ('O mais velho do grupo chama {} e tem {} anos'.format(nomevelho,homemvelho))
input()