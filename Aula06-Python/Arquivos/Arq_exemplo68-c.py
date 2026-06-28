import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio")
print(diretorioCorrente)

texto = """ Hoje, é um bom dia para aprender Python
Principais caracteristicas
Vantagens e desvantagens 
"""


'''
opção with, É fundamental e lembrar de fechar o arquivo se não 
ao sair do interpretador ou do programa em execução iremos perder 
todas as escritas feitas no arquivo. 
'''
with open('Aula06-String_Arquivos-Python/Arquivos/arquivo3.txt', 'r+', encoding='utf-8') as arqEscrita:
	arqEscrita.write(texto)
	conteudo = arqEscrita.readlines()
	print("\n Relatorio do arquivo\n")

	palavra = input("Digite a palavra que gostaria de buscar = ")
	contador_linhas=0
	for linha in conteudo:
		linha = linha.rstrip()
		if palavra in linha:
			contador_linhas = contador_linhas+1
			print(contador_linhas)
	#print("O Arquivo tem = " + str(contador_linhas) + " linhas")

print("Operação concluida com sucesso no arquivo =" ,arqEscrita.name, "Modo de Leitura = ", arqEscrita.mode, "Arquivo está fechado ?=", arqEscrita.closed)

