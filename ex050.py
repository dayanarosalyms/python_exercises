s = 0
for num in range(1,7):
    print(input('Digite um numero: '))
    if num % 2 == 0:
        s = s + num
        print(f'A soma dos numeros pares é {s}')