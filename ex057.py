sexo = str(input('Informe seu sexo:[M/F]: ')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso. ')