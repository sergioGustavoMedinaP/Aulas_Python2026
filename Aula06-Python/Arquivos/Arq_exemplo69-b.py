import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio")
print(diretorioCorrente)

with open('Aula06-String_Arquivos-Python/Arquivos/filmes.txt', 'a+', encoding='utf-8') as arq:
  arq.write("Vingadores \n")
  arq.write("Vingadores II\n")
  arq.write("Vingadores III\n")

print("Operação concluida com sucesso no arquivo =" ,arq.name, "Modo de operação = ", arq.mode, "Arquivo está fechado ?=", arq.closed)


with open('Aula06-String_Arquivos-Python/Arquivos/filmes.txt', 'r+', encoding='utf-8') as arqLeitura:
	conteudo = arqLeitura.readlines()
	print("\n Relatorio dos filmes cadastrados\n")

for linha in conteudo:
	  linha = linha.rstrip()  # (),  # que elimina espaços no início de uma string, pois os caracteres \n  são tratados com espaços
	  print(linha)

print("Operação concluida com sucesso no arquivo =" ,arqLeitura.name, "Modo de operação = ", arqLeitura.mode, "Arquivo está fechado ?=", arqLeitura.closed)

