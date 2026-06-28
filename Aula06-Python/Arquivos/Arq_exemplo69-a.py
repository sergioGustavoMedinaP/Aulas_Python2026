import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio")
print(diretorioCorrente)

with open('Aula06-String_Arquivos-Python/Arquivos/filmes.txt', 'w', encoding='utf-8') as arqEscrita:
    arqEscrita.write('Tubarão\n')
    arqEscrita.write('O Podereso Chefão\n')
    arqEscrita.write('De Volta Para O Futuro I\n')
    arqEscrita.write('De Volta Para O Futuro II \n')
    arqEscrita.write('De Volta Para O Futuro III \n')
    print("Operação concluida com sucesso no arquivo =" ,arqEscrita.name, ", O Modo de Leitura = ", arqEscrita.mode, "Arquivo está fechado ?=", arqEscrita.closed)
print("Operação concluida com sucesso no arquivo =" ,arqEscrita.name, "Modo de Leitura = ", arqEscrita.mode, "Arquivo está fechado ?=", arqEscrita.closed)

with open('Aula06-String_Arquivos-Python/Arquivos/filmes.txt', 'r+', encoding='utf-8') as arqLeitura:
	conteudo = arqLeitura.readlines() # arqLeitura,read()
    #print("Saida 1: ", conteudo)
	#print("\n Relatorio do arquivo\n")

print("\n Relatorio dos filmes cadastrados\n")
for linha in conteudo: #itemLinha elemento
	linha = linha.rstrip()  # (),  # que elimina espaços no início de uma string, pois os caracteres \n  são tratados com espaços
	print(linha)

print("Conteudo da lista = ", conteudo)

print("Operação concluida com sucesso no arquivo =" ,arqLeitura.name, "Modo de Leitura = ", arqLeitura.mode, "Arquivo está fechado ?=", arqLeitura.closed)