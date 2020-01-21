#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
print ('-='*10)
print ('FACTORIAL!!')
print ('-='*10)
n = int(input('Digite o número: '))
print ('{}! = '.format(n),end='')
c = n
f = 1
while c > 0:
    print ('{} '.format(c),end='')
    print ('X 'if c > 1 else '=',end='')
    f *= c
    c -= 1
print (' {}'.format(f))