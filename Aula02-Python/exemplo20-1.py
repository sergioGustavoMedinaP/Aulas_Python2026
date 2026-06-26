"""
print("Parte I - Entrada de dados via teclado")

nome = "Carlos"
sobrenome = "Silva"

print("1ra Saida: ", nome, sobrenome)
print("2da Saida: ",nome, sobrenome, sep="-" )
print("3ra Saida: ",nome, sobrenome, sep="           ", )
print("Tipo da variavel nome = ",type(nome))
print("Tipo da variavel sobrenome = ",type(sobrenome))
print("")
print("Parte II")
sujeito = "Python"

verbo = "é"
predicado= "fantástico"
print(sujeito, verbo, predicado, sep="-", end="!\n")
print(sujeito+" "+ verbo+" "+predicado)
print("")

"""
print("Parte III")
print("Processo de autenticação. Favor digitar o seu login e senha")
var_login = input("Login:")
var_senha = input("Senha:")

print("Os dados digitados: ")

print("Login =  %s, e senha = %s" %(var_login, var_senha))

divisao1 = 5/3
divisao2 = 5//3

print("Divisão de 5/3 = %i" %divisao1, type(divisao1))
print("Divisão de 5//3 = ",type(divisao2))
print(round(divisao2, 3))


print(4%3)



