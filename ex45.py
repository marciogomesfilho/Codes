from random import randint
from time import sleep
pc = randint(1,3)
jogador = str(input( 'Papel, pedra ou tesoura?\n')).lower().strip()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
if pc == 1 and jogador == 'pedra':
    print ('O computador \033[4;32mganhou\033[m!\nO computador escolheu papel')
    input()
elif pc == 1 and jogador == 'papel':
    print('\033[1;31mEMPATOU\033[m!!\nO computador também escolheu papel!')
    input()
elif pc == 1 and jogador == 'tesoura':
    print('Você \033[4;32mganhou\033[m!\nO computador escolheu papel')
    input()
elif pc == 2 and jogador == 'tesoura':
    print ('\033[1;31mEMPATOU\033[m!!\nO computador também escolheu tesoura!')
    input()
elif pc == 2 and jogador == 'pedra':
    print('Você \033[4;32mganhou\033[m!\nO computador escolheu tesoura')
    input()
elif pc == 2 and jogador == 'papel':
    print('O computador \033[4;32mganhou\033[m!! Ele havia escolhido tesoura')
    input()
elif pc == 3 and jogador == 'pedra':
    print ('\033[1;31mEMPATOU\033[m! \n O computador escolheu pedra também')
    input()
elif pc == 3 and jogador == 'papel':
    print ('Você \033[4;32mganhou\033[m!\nO computador escolheu pedra')
    input()
elif pc == 3 and jogador == 'tesoura':
    print ('O computador \033[4;32mGANHOU\033[m!\nEle escolheu pedra')
else:
    print('JOGADA INVALIDA')
    input()



"""from random import randint

pc = randint(0,2)
itens = ('pedra', 'papel', 'tesoura')

print ('o computador escolheu: {} '.format(itens[pc]))"""







