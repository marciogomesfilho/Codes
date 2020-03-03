principal = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1+nota2)/2
    principal.append([nome,[nota1,nota2],media])
    continuar = str(input('Deseja continuar? [S/N]: '))
    if continuar in 'Nn':
        break
print ('-='*11)
print (f'{"BOLETIM":^22}')
print ('-='*11)
print (f'{"Nº":<4}{"Nome":<7}{"Média":>11}')
for i,a in enumerate(principal):
    print (f'{i:<4}{a[0]:<7}{a[2]:>11}')
while True:
    opcao = int(input('Deseja ver a nota de qual aluno? (999 interrompe): '))
    if opcao == 999:
        print ('FIM DO PROGRAMA')
        break
    if opcao <= len(principal) - 1:
        print (f'A nota do(a) aluno {principal[opcao][0]} foi {principal[opcao][1]}')
        continue
print ('VOLTE SEMPRE!!!')