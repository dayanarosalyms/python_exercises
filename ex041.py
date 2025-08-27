from datetime import datetime
agora = datetime.now()
ano_atual = agora.year
nascimento = int(input('Qual ano você nasceu? '))
idade = ano_atual - nascimento
print(f'Você nasceu em {nascimento} e tem {idade} anos.')
if idade <=9:
    print('Você  é da categoria MIRIM.')
elif idade <=14:
    print('Você é da categoria INFANTIL.')
elif idade <=19:
    print('Você é da categoria JUNIOR.')
elif idade == 20:
    print('Você é da categoria SENIOR.')
else:
    print('Você é da categoria MASTER')