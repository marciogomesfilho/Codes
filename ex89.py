"""


"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
"""
completa = list()
temp = list()
resposta = list()
media = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a 1 nota: '))
    nota2 = float(input('Digite a 2 nota: '))
    media = (nota1+nota2)/2
    temp.append([nome], [nota1, nota2], [media])
    completa.append(temp[:])
    temp.clear()
    resposta.append(f'Nome:{nome}||Média:{media}')
    continuar = str(input('Deseja continuar? (S/N): '))
    if continuar in 'Nn':
        break
print (resposta)
print(completa)


"""opcao = str(input('Deseja ver as notas de um aluno em especifico? [S/N]: '))
if opcao in 'Ss':
    while True:
        opcao2 = str(input('Digite o nome do aluno ou [N/n] para finalizar: ')).upper()
        if opcao2 not in 'nN':
            print (f' O aluno {nome} teve as notas {completa[0][1]} e {completa[0][2]}.')
            opcao2 = str(input('Digite o nome do aluno ou [N/n] para finalizar: ')).upper()
        else:
            break
print ('FIM DO PROGRAMA')
input()
else:
    print('FIM DO PROGRAMA')
    input()"""""



   # ""while True:
    #    opcao3 = str(input('Deseja ver de outro aluno? [S/N]: '))
     #   opcao3 = str(input('Digite o nome do aluno: ')).upper()
      #  print(f' O aluno {opcao3} teve as notas {completa[0][1]} e {completa[0][2]}.')
       # if opcao3 in 'Nn':
       #     break"""""
""""""