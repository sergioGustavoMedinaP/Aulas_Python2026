texto_aspas_simples = 'Texto entre "aspas" Simples'
texto_2aspas_duplas= "Texto 'entre' 'aspas' Dupla"
texto_3aspas_simples = '''
String com 3 aspas Simples,
texto22,
texto33,
texto44
'''

texto_3aspas_duplas = """
String com 3 aspas Duplas,
textoAA,
textoBB,
textoCC
"""

print("1ro texto = " + texto_aspas_simples)
print("2do texto = " + texto_2aspas_duplas)
print("3ro texto = " + texto_3aspas_simples)
print("4to texto = " +texto_3aspas_duplas)



print("\n ------------------------\n")
texto1 = "10"
num1 = 10
num2 = 20.2
texto2 = "20.2"

num = int(texto1)
valor = float(texto2)
#print()
print("\n Valor de variável texto1 = " +texto1)
print("Tipo da variavel texto1 = ", type(texto1))
#print()
print("\n Valor de variável num = " , num)
print("Valor de variável num = " +str(num))
print("Tipo da variavel num = ", type(num))
#print()
print("\n Valor da variável valor = ",valor)
print("Tipo da variavel valor = ", type(valor))

