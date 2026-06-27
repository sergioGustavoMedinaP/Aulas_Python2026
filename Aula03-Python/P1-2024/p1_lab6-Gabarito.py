estoqueFrutas1 = {'kiwis': 30,
    'bananas': 112,
    'laranjas': 525,
    'peras': 217
}

estoqueFrutas2 = {'mangas': 130,
        'abacaxis': 150,
        'uvas': 325,
        'ameixas': 517,
        'melancia': 200,
}

print("Conteúdo completo do dicionário (estoque 1) = " , estoqueFrutas1)

estoqueFrutas1['bananas'] = estoqueFrutas1['bananas'] + 200

for frutas, quantidade1 in estoqueFrutas1.items():
     print(frutas +"= " +str(quantidade1))

numItensEstoque1 = len(estoqueFrutas1)
print("Numero de itens no estoque 1= " , numItensEstoque1)

print("Conteúdo completo do dicionário (estoque 2) = " , estoqueFrutas2)
for frutas, quantidade2 in estoqueFrutas2.items():
     print(frutas +"= " +str(quantidade2))

print(" Lista de frutas do estoque 2: ", list(estoqueFrutas1.keys()))
print()

numItensEstoque2 = len(estoqueFrutas2)
print("Numero de itens no estoque 2= " , numItensEstoque2)

if ("melancia" in estoqueFrutas2.keys()):
     print("Tem " +str(estoqueFrutas2["melancia"]) + " melancias no estoque  2")
else:
    print("Não tem")

print("Calculo da Soma (total) de frutas no estoque de frutas1 + estoque de frutas2")
estoqueFrutas1.update(estoqueFrutas2)

print("Total de frutas no estoque 1 ",estoqueFrutas1)
numItensEstoque1 = len(estoqueFrutas1)
print("Numero de itens no estoque 1= " , numItensEstoque1)
