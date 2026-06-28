import os

diretorioCorrente = os.getcwd()
print("Vc está no seguinte diretorio =", diretorioCorrente)

arq = open('Aula06-String_Arquivos-Python/Arquivos/arquivo.txt', 'r', encoding="utf-8")

conteudo = arq.readlines()
print("\n Conteudo da variavel conteudo \n", conteudo)

'''
Função: método rstrip()
Podemos eliminar essa linha em branco usando o método rstrip(), 
que elimina espaços no início de uma string, pois os caracteres \n 
são tratados com espaços
'''
print("\n Relatorio do lista_arquivo\n")
for item in conteudo:
    item = item.rstrip()
    print(item)

print("O arquivo está fechado?".format(arq.closed))
if not arq.closed:
  arq.close()

print('Estado atual Arquivo = {}'.format(arq.closed))



