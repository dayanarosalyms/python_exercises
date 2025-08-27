distancia = int(input('Quantos kms de distância até seu destino? '))
if distancia >= 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.50

print(f'Sua passagem custará {preco:.2f} reais. ')