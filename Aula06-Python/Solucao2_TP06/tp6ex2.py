arquivo = open('carros.txt', 'r', encoding='utf-8')
texto = arquivo.read()
arquivo.close()

lista = texto.split('\n')

segundo_arquivo = open('invertido.txt', 'w', encoding='utf-8')
for i in range((len(lista))-1,-1,-1):
    segundo_arquivo.write(lista[i] + ('\n' if i != 0 else ''))
segundo_arquivo.close()

print('ordem invertida')

terceiro_arquivo = open('ordenado.txt', 'w', encoding='utf-8')
ordenado = sorted(lista)
for i, carros in enumerate(ordenado):
    terceiro_arquivo.write(ordenado[i] + ('\n' if i < len(ordenado)-1  else ''))
terceiro_arquivo.close()

print('carros ordenados')