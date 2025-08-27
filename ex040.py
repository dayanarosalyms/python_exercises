n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'Sua média final é {media:.2f}. Você foi reprovado!')
elif media >= 5 and media < 7:
    print(f'Sua média final é {media:.2f}. Você está em recuperação!')
else:
    print(f'Sua média final é {media:.2f}. Você foi aprovado! Parabéns!')
