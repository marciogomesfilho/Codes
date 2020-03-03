#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""expressao = str(input('Digite sua expressão: '))
parent1 = list() #(
parent2 = list() #)
if '(' or ')' in expressao:
    parent1.append('(' in expressao)
    parent2.append(')' in expressao)
else:
    print ('Não há parenteses na expressao')
print (parent1)
print (parent2)""" #TENTATIVA QUE NAO DEU CERTO

#tentativa que deu certo porem nao utiliza lista

"""expressao = str(input('Digite sua expressão: '))
a = (expressao.count('('))
b = (expressao.count(')'))
if a == b:
    print ('Expressão válida!')
else:
    print ('Expressão invalida!')"""

#MANEIRA CERTA USANDO LISTA


"""expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
if len(pilha) == 0:
    print ('exptrssao valida')
else:
    print ('expressao invaida')"""



expr = str(input('Digite a expressão: '))
pilha = []
    for simb in expr:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
    if len(pilha) == 0:
        print ('Expressão válida ! ')
        input()
    else:
        print ('Expressão inválida')
        input()











