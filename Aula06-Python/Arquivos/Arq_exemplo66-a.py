#Exemplo 66-a
import os

diretorio_corrente = os.getcwd()         # cwd = Current Working Directory
print("Vc está neste diretorio")
print("Diretorio Atual = "+diretorio_corrente) # pwd = Present Working Directory
#arq = open('arq01.txt', 'r', encoding="utf-8")

arq = open('Aula06-String_Arquivos-Python/Arquivos/arq01.txt', 'r', encoding="utf-8")

print("\n Método read(), arq.read: \n")
saudacao = arq.read()

print("\nTipo da arq = ", type(saudacao))
print("\n-------Inicio da Saida do arquivo ------\n" +saudacao)
print("\n-------Fim da arquivo ------------------\n")

print("Tamanho da variavel saudacao = ", len(saudacao))
print("Posição atual no arquivo = " ,arq.tell())
print("Volta a posição inicial da variavel no saudacao =", arq.seek(0))

lista_arquivo = saudacao.split('\n')
print("\n---Retorna o conteudo do arquivo em forma de lista--- \n",lista_arquivo)
print("\n---Retorno a linha 4 -------\n", lista_arquivo [3])
print("Id do processo arq =", id(arq))
print("Id do processo lista_arquivo =",id(lista_arquivo))
arq.close()
