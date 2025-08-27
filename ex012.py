preco= float( input('Qual é o preço do produto? '))
novo= preco - (preco * 5/100)
print('O produto que custava {}, na promoçao com desconte de 5% vai custar R${}'.format(preco,novo))