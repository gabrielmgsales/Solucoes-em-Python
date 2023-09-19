largura = float(input('Qual é a largura da parede: ').replace(',','.'))
altura = float(input('Qual é a altura da parede: ') .replace(',','.'))
area = largura * altura

print ('A área total da parede é de {:.2f} m²'.format(area))

tinta = area / 2

print ('Para pintar essa área você precisará de {:.2f} lts de tinta'.format(tinta))