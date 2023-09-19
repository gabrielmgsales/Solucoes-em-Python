real = float(input('Quanto deseja converter ? R$').replace(',', '.'))
dolar = real / 4.86

print ('Com R${:.2f} você poderá comprar U$${:.2f}'.format(real, (real/4.86)))
