# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).

nome = str(input('Digite seu nome: ')).strip()
print('Seu nome maiusculo é: {} '.format(nome.upper()))
print('Seu nome minusculo é: {} '.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print ('seu primeiro nome é {} e tem {} letras'.format(separa[0], len(nome)-nome.count(' ')))
