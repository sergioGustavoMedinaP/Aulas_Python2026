#Exemplo 66-c
import os

diretorioCorrente = os.getcwd()         # cwd = Corrent Working Directory
print("Vc está no seguinte diretorio = ", diretorioCorrente)   # pwd = Present Working Directory

arq = open('Aula06-String_Arquivos-Python/Arquivos/arq01.txt', 'r', encoding="utf-8")

lista_saudacao = arq.readlines()
print("Posição atual no arquivo: ", arq.tell())
print("\nConteudo do arquivo arq01 ------\n", lista_saudacao)

print("Volta a posição inicial no saudacao = ", arq.seek(0))

arq.close()

