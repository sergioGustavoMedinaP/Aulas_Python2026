'''
A tabela ASCII contém os caracteres vinculados a um número inteiro
positivo.
Essa tabela decorre do fato de que o computador só manipula números, 
logo, cada caractere, possui, um número que o identifique.

O termo ASCII é um acrônimo de American Standard Code for Information
 Interchange que numa tradução livre, seria, "Código Padrão Americano 
 para o Intercâmbio de Informação".
'''

print("O Resultada da comparação entre (A == A) = " + str("A" == "A") )# True
print("O Resultada da comparação entre (b == b) = " + str("b" == "b")) # True
print ("O Resultada da comparação entre (a > c) = " + str("a" > "c"))# False
print ("O Resultada da comparação entre (C > a) = " + str("C" > "a")) # False


print ("Valor do decimal da letra a = ", ord('a'))  # 97
print ("Valor do decimal da letra c = ", ord('c'))  # 99
print ("Valor do decimal da letra A = ", ord('A'))  # 65

print("Conversão do valor decimal 97 caracter = ", chr(97) ) # 'a'
print("Conversão do valor decimal 65 caracter = ", chr(65) ) # 'A'
print("Conversão do valor decimal 99 caracter = ", chr(99) ) # 'c'

print("Conversão do valor decimal 60 para caracter = ", chr(60))  
print("Conversão do valor decimal 62 para caracter = ", chr(62))

for c in range(256): # vi = 0, vf<256, step = 1
  print(str(c) + " == " + chr(c))
