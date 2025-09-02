senhas = ["abc", "segura123","12345", "python123", "oi"]
for senha in senhas:
    if len(senha) > 6:
        print(f'A senha \"{senha}\" é válida')
    else:
        print(f'A senha \"{senha}\" deve possuir no mínimo 6 caracteres.')