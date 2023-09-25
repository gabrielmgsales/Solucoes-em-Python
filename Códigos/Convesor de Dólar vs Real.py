real = float(input('Quanto deseja converter ? R$').replace(',', '.'))
dolar = real / 4.86

print (f'Com R${real:.2f} você poderá comprar U$${dolar:.2f}')
