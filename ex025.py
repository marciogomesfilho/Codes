# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.


nome = str(input('digite seu nome: ')).strip()

print('seu nome tem siva? {}'.format('silva' in nome.lower()))
