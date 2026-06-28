"""

'''
A função split( ) divide um texto todas as vezes que a String 
passada como argumento for localizada. 
'''

texto = "Toda string em Python é imutável"
print("conteudo original da variavel texto =" + texto)
nova_lista = texto.split() # divide um texto todas as vezes que a String passada como argumento for localizada
print(" Nova variavel nova_lista = ", nova_lista)

print("Saida 1 = " ,texto.split(" ")) # definindo como argumento, uma String que contém um único espaço em branco.
print("Saida 2 = " ,nova_lista)
print(nova_lista[3] +" "+ nova_lista[5])
teste =nova_lista[3] +" "+ nova_lista[5]
print("Id da variavel teste", id(teste))
print("Id da variavel texto = ", id(texto))
print("Id da variavel novaLista =", id(nova_lista))

"""

'''
A função replace() substitui uma parte do texto por uma outra String. 
A palavra replace(), do Inglês, significa substituir e
é isso que a função replace() da classe String do Python faz.
'''

s = "A função replace aa substitui parte de um texto por outro texto"
s2= s.replace("aa", "@@")

print("Frase original = " +s)
print("Frase alterada = " + s2)
# 'A função replace 123 substitui parte de um texto por outro texto'

print ("Tamanho da variavel s = " ,len(s))
print("Tamanho da variavel s2 = " , len(s2))
print(id(s))
print(id(s2))

