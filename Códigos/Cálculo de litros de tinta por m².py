largura = float(input('Qual é a largura da parede: ').replace(',','.'))
altura = float(input('Qual é a altura da parede: ') .replace(',','.'))
area = largura * altura

print (f'A área total da parede é de {area:.2f} m²')

tinta = area / 2

print (f'Para pintar essa área você precisará de {tinta:.2f} lts de tinta')
