#troca de valores das variáveis caso A seja maior do que B
A = int(input('Informe um valor para a variável A: '))
B = int(input('Informe um valor para a variável B: '))

if (A>B):
    aux = A
    A=B
    B=aux
print(f'O valor da variável A agora é {A}')
print(f'O valor da variável B agora é {B}')