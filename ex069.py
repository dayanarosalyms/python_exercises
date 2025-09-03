
try:
    a = int(input('Digite A:'))
    b = int(input('Digite B: '))
    r = a / b
    print(b)
except ZeroDivisionError:
    print('P valor de B não pode ser zero. ')
except ValueError:
    print('Digite numeros inteiros para A e B. ')
except:
    print('Não é possivel calcular a divisão.')
print('Fim do programa!')