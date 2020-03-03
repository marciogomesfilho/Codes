"""Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves."""
lista = list()
temp = list ()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    lista.append(temp[:])
    temp.clear()
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
print (f'A quantidade de pessoas cadastradas foi: {len(lista)} pessoas')

print ('Pessoa(s) mais gorda(s):\n',end='')
for p in lista:
    if p[1] == mai:
        print (f'{p[0]}')
print ('\nPessoa(s) mais leve(s):\n',end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}')