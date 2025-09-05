n = -1
while n != 0:
    n = int(input('Digite um numero: '))
    match n:
        case 1:
            print('voce digitou o numero 1.')
        case 2:
            print('voce digitou o numero 2.')
        case 3:
            print('voce digitou o numero 3')
        case _:
            print('voce digitou outra coisa.')