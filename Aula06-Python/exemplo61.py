"""
Concatenar é a junção de 2 cadeias de caracteres e que dá origem a uma nova string que é formada pela junção das 2 partes. 
A concatenação, pode ser a direita ou então a esquerda de outra string. 
Então por exemplo, a listagem 4, temos um exemplo em que fazemos alguns tipos de concatenações.
"""

print("Parte I")
s = "Lista de Caracteres em Python"
print("Resultado da variavel s =" +s)

print("Parte II") #concatenação de 2 trechos de texto
texto1 = "123"
texto2 =  "456"

num1 = 5
num2 = 6
resultado = num1 + num2
print("Resultado da soma = ", resultado)
concatenacao =  texto1 + texto2
print("Resultado da variavel concatenação = " +concatenacao) # Saida = '123456'

id(num1)
print("Numero de identificação de um processo (num1) = ", id(num1))
print("Numero de identificação de um processo (num2) = ", id(num2))
print("Numero de identificação de um processo (texto1) = ", id(texto1))
print("Numero de identificação de um processo (texto2) = ", id(texto2))

a = "bra" #declaração da variável `a` que foi associado ao texto `bra`
b = "sil" #declaração da variável `b` que foi associado ao texto `sil`

#ao escrevemos no prompt a + b temos que é impresso a CONCATENAÇÃO
print("concatenação de a + b = " + (a + b))   # Saida = 'brasil'
c = a + b #agora, concatenamos e o resultado associamos a variável `c`
print("Resutado da variavel c = " + c) #Saida = 'brasil'
#agora, podemos dizer que o trecho de texto `bra`
# foi adicionado a esquerda da variável `b`
print("concatenação de b + a = " +(b + a)) #Saida ='silbra'



