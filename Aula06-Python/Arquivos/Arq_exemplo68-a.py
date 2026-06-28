import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio")
print(diretorioCorrente)

texto = '''Boa noite.
Vc está preparado para uma imersão em Python?
Python foi criada por Guido Van Rossum
a comunidade Python é muito legal
'''
arq = open('Aula06-String_Arquivos-Python/Arquivos/arquivo2.txt', 'a+', encoding='utf-8')
arq.write(texto)
print("Operação de escrita, realizada com sucesso")
print('O arquivo está fechado?'.format(arq.closed))

if not arq.closed:
  arq.close()

print('Estado atual Arquivo = {}'.format(arq.closed))
print("Operação concluida com sucesso no arquivo =" ,arq.name, "Modo da estrutura = ", arq.mode)



arq2 = open('Aula06-String_Arquivos-Python/Arquivos/arquivo2.txt', 'r', encoding='utf-8')

conteudo1 = arq.readline()

# Para obter a posição corrente em um arquivo utilizamos o método tell( ), que retorna um inteiro medido em bytes a partir do início do objeto file. 
linha = arq2.tell()
conteudo2 = arq2.readlines()
print("\n Posição corrente da linha do arquivo arq.write()= ", linha)
print("\n Saida 1: Conteudo do arquivo arq.write(): \n", conteudo1)
print("\n Saida 2: Conteudo do arquivo arq.write(): \n", conteudo2)

print("\n Saida 3:  Relatorio do arquivo\n")
for linha in conteudo2:
	linha = linha.rstrip()  # (),  # que elimina espaços no início de uma string, pois os caracteres \n  são tratados com espaços
	print(linha)


print('O arquivo está fechado?'.format(arq2.closed))
if not arq2.closed:
  arq2.close()

print('Estado atual Arquivo = {}'.format(arq2.closed))

print("Operação concluida com sucesso no arquivo =" ,arq.name, "Modo de operação = ", arq2.mode, "Arquivo está fechado ?=", arq2.closed)


