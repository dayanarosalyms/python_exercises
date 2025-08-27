from random import randint
from time import sleep
computador = randint(1,5)
print('-=-'*20)
print('BORA JOGAR! ')
print('Irei pensar em um número entre 1 e 5! Tente advinhar...')
print('-=-'*20)
jogador = int(input('Qual número eu pensei?  '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('VOCE ACERTOU! PARABÉNS!')
else:
    print('VOCÊ ERROU! LOSER! ')
    print(f'Eu pensei no numero {computador} e não no número {jogador}!')

