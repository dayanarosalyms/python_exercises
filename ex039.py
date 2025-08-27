from datetime import datetime
nascimento = int(input('Qual seu ano de nascimento? '))
calculoid =  2025 - nascimento
print(f'Você nasceu em {nascimento} então tem {calculoid} anos!')
if calculoid == 18:
    print('É HORA DE ALISTAR!')
elif calculoid < 18:
    print('Você ainda vai se alistar!')
    aindafalta = 18 - calculoid
    print(f'Ainda faltam {aindafalta} anos para você se alistar!')
else:
    print('Já passou da hora de se alistar!')
    agora = datetime.now()
    anoatual =agora.year
    anoalistamento = nascimento + 18
    passou = anoatual - anoalistamento
    print(f'Já passou {passou} anos.')