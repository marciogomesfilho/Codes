#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos. #B) quantos homens foram cadastrados. #C) quantas mulheres tem menos de 20 anos.
idade = 0
sexo = ''
continuar = ''
maior = homem = mulheres = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    if continuar in 'nN':
        break
print (f'Pessoas com mais de 18 anos: {maior}\nHomens: {homem}\nMulheres com menos de 20 anos: {mulheres}')