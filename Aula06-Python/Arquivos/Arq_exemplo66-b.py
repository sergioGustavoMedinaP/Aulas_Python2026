#Exemplo 66-b
"""
import os

diretorio_corrente = os.getcwd()
print("Vc está neste diretorio")
print("Diretorio Atual = "+diretorio_corrente)
arq = open('Aula06-String_Arquivos-Python/Arquivos/arq01.txt', 'r', encoding="utf-8")

print("\nMétodo readline(), arq.readline:\n")
saudacao = arq.readline()  #linha 0
print("1ro Conteudo da variavel saudação = ", saudacao)
saudacao = arq.readline()  #linha 1
print("2do Conteudo da variavel saudação = ", saudacao)
saudacao = arq.readline()  #linha 2
print("3ro Conteudo da variavel saudação = ", saudacao)
print("Posição atual no arquivo saudacao = ", arq.tell())

print("Volta a posição inicial da variavel no saudacao: ", arq.seek(0))

lista_saudacao = saudacao.split('\n')  #saudacao.split()
print("\n--Retorno 1 do conteudo do arquivo em forma de lista ----\n", lista_saudacao)
lista_saudacao2 = saudacao.split()
print("\n--Retorno2 do conteudo do arquivo em forma de lista ----\n",lista_saudacao2)
arq.close()
"""

import os

diretorioCorrente = os.getcwd()
print("Vc está neste diretorio")
print("Diretorio Atual = "+diretorioCorrente)
arq = open('Aula06-String_Arquivos-Python/Arquivos/arq01.txt', 'r', encoding="utf-8")

saudacao = arq.readline() # arq.read()
saudacao = arq.readline() 
saudacao = arq.readline() 
print("\nConteudo da variavel saudacao\n")
print(saudacao)

lista_arquivo = saudacao.split()
print("\n Relatorio do arq com o Método readline()\n")
cont = 0
for elemento in lista_arquivo:
    print ("Conteudo da variavel linha = ", elemento)
    cont = cont +1

print("Conteudo da variavel saudacao = ",saudacao)
print("O total de elemento da lista  = ",cont)
print("Conteudo da variavel lista_arquivo = ",lista_arquivo)
arq.close()

