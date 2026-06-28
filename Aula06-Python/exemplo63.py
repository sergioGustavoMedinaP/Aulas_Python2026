texto = "Toda string em Python é imutável"

print("Frase completa = " +texto)
print("Retorna o primeiro caractere da variavel texto = " +texto[0]) #retornando o primeiro caractere
# Saida = 'T'

print("Retorna o último caractere da variavel texto = " +texto[-1]) #retornando o último caractere
# Saida ='l'

print("Tamanho da variavel Texto = " , len(texto))

print("Retorna os caracteres da variavel texto  entre as posições 15 até 21 = " +texto[15:21])
# Saida ='Python'

print("Retorna os caracteres da variavel texto  entre as posições 5 até o final = " +texto[5:])
print("Retorna o texto de forma invertida = " +texto[ : : -1])

tamanho = len(texto)
print("Comprimento total da variavel texto = " +str(len(texto)))
print("Resultado da variavel tamanho = " +str(tamanho))
print(texto[5])
print(texto[7])

print(texto[::-1])
print(texto[0:10:2]) # vi= 0, vf=10 , step = 2

#texto[5] = "x" #Cuidado!!!
print(id(texto))
