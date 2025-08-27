from datetime import date
nasc = int(input(' Em que ano a pessoa nasceu? '))
atual = date.today().year
for pess in range(1,8):
    idade = atual -nasc
    print(f'Essa pessoa tem {idade}')
    if idade >= 21:
        print('maior de idade')
    else:
        print('menos de idade')