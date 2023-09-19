preco = float(input('Digite o preço sem o desconto: R$').replace(',','.'))
desconto = int(input('Qual é a porcentagem de desconto: ').replace(',','.'))
porcentos = preco * desconto / 100
novo = preco - porcentos

print('Preço do produto: R${:.2f}'.format(preco))
print('Desconto de {}% = -R${}'.format(desconto, porcentos))
print('Total a pagar: R${}'.format(novo))