"""pessoa = {'nome': 'Marcio', 'idade': 22, 'sexo': 'M'}
print (f'O {pessoa["nome"]} tem {pessoa["idade"]} e é do sexo {pessoa["sexo"]}')
pessoa ['peso'] = 60.5
for k, v in pessoa.items():
    print (f'{k} = {v}')"""
"""brasil = []
estado1 = {'UF': 'Rio de Janeiro','sigla':'RJ'}
estado2 = {'UF': 'Sao Paullo', 'sigla':'SP'}
print (estado1,estado2)
brasil.append(estado1)
brasil.append(estado2)
print (brasil[0]['UF'])"""

"""estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print (f'O campo {k} tem valor {v}')"""

# Faça um programa que leia nome e media de um aluno guardando tambem a situacao e diga se ele foi aprovado ou nao
lista = list()
dicio = dict()
situacao = ''
dicio['nome'] = str(input('Nome: '))
dicio['media'] = float(input('Média: '))
if dicio['media'] >= 7:
    situacao = 's'
else:
    situacao = 'n'
dicio['status'] = situacao
print (f'Nome é igual a {dicio["nome"]}')
print (f'Média é igual a {dicio["media"]}')
if situacao == 's':
    print (f'Situação é igual: Aprovado')
else:
    print (f'Situação é igual: Reprovado')








