soma = 0

for c in range(1, 501):  # vai de 1 até 500
    if c % 2 != 0 and c % 3 == 0:  # verifica se é ímpar e múltiplo de 3
        soma += c  # adiciona o número à soma

print(f"A soma dos números ímpares múltiplos de 3 entre 1 e 500 é {soma}")
