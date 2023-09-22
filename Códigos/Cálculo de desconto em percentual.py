preco = float(input('Digite o preço sem o desconto: R$').replace(',','.'))
desconto = int(input('Qual é a porcentagem de desconto: ').replace(',','.'))
porcentos = preco * desconto / 100
novo = preco - porcentos

print(f'Preço do produto: R${preco:.2f}')
print(f'Desconto de {desconto:.1f}% = -R${porcentos}')
print(f'Total a pagar: R${novo:.2f}')
