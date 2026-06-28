arquivo = open('carros.txt', 'w')
lista = ['• Gol','• Uno','• Palio','• EcoSport','• Clio','• Strada','• Golf']

for i, carro in enumerate(lista):
    arquivo.write(carro + ('\n' if i < len(lista)-1 else ''))
arquivo.close()

print('lista criada')