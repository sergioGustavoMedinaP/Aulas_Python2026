import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio = ", diretorioCorrente)

with open('Aula06-String_Arquivos-Python/Arquivos/arquivo.txt', 'r', encoding='utf-8') as arq:
	#print(arq.read())
	#print(arq.readline())
	#print(arq.readlines())

	conteudo = arq.readlines()
	#onteudo = arq.seek(0)
	#conteudo = arq.readlines()
	
	print("\n Conteudo do arquivo\n")
	for linha in conteudo:
		linha = linha.rstrip()
		print(linha)


