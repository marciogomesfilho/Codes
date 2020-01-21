#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""for c in range(1, 10):
    print(c)
print ('Fim')"""
###############################################
"""c = 1
while c < 10:
    print (c)
    c = c + 1
print ('Fim')"""
################################################
sexo = str(input('Digite seu sexo (M/F): ')).upper().strip()
while sexo not in 'mMFf':
    sexo = str(input('Tente novamente.'))
print('Sexo cadastrado')
