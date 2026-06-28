"""
Interpolar é a inserção de um trecho de texto dentro de outro. 
A interpolação, ocorre de várias formas, e, algumas linguagens e bibliotecas, proporcionam maneiras bastante interessantes e diferentes para interpolarmos valores. 
O Python fornece um conjunto de ferramentas bastante poderosas para esse fim
"""

sexo = "masculino"
nome = "Luiz Antônio de Oliveira Gomes (RA:D65857-3)"
idade = 20

interpolar1 = "Sexo é igual a %s,  o nome é igual %s com idade = %i anos" %(sexo, nome, idade)
concatenar = sexo + " " + nome
print("Saida 1 da interpolação1 = " +interpolar1)
print("Saida 2 da concatenação = " +concatenar)

"""
agora, vamos colocar uma String entre chaves dentro do texto
em seguida, com a função format(), vamos associar
os nomes definidos entre chaves a texto passando-os
como argumentos de função
"""

interpolar2 = "Sexo é igual a {SEXO} e o nome é igual {NOME} com idade {IDADE} anos ".format(SEXO=sexo,NOME=nome, IDADE= idade)
print("Saida 2 da interpolação2 = " +interpolar2)

#Saida = 'Sexo é igual a masculino e o nome é igual Henrique '
