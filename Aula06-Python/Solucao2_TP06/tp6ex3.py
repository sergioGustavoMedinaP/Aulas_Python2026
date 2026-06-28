arquivo = open('notas_estudantes.dat', 'w', encoding='utf-8')
aluno = 'Jose,3.5,0.0,5.5,1.5\nPedro,7.5,2.0,7.5,1.0\nSuzana,6.5,1.5,5.5,1.5\nGisela,8.0,2.0,7.5,1.0\nJoão,3.5,0.0,5.5,0.0\nAndre,6.0,1.5,7.0,1.0\nCarlos,1.5,0.0,4.0,0.0\nNatalia,6.0,2.0,5.5,1.5'
arquivo.write(aluno)
arquivo.close()

arquivo = open('notas_estudantes.dat', 'r', encoding='utf-8')
texto = arquivo.read()
linhas = texto.split('\n')
for i, linha in enumerate(linhas):
    linhas[i] = linha.split(',')

for i, linha in enumerate(linhas):
    linhas[i].append((float(linha[1]) + float(linha[2]) + float(linha[3]) + float(linha[4]))/2)
    print('aluno '+ linha[0] + " media geral ",linha[5])

for i, linha in enumerate(linhas):
    if linha[5] >= 7:
        print('aluno '+ linha[0] + " foi aprovado " )


max_coluna = 0
for i in range(0,len(linhas)-1,1):
    max_coluna = linhas[i][5] if linhas[i][5] > max_coluna else max_coluna

min_coluna = max_coluna
for i in range(0,len(linhas)-1,1):
    min_coluna = linhas[i][5] if linhas[i][5] < min_coluna else min_coluna

print('o minimo da turma é',min_coluna,' o maximo da turma é ',max_coluna)

for i, linha in enumerate(linhas):
        nota_minima = 0
        nota_maxima = 0
        p1 = float(linha[1]) + float(linha[2])
        p2 = float(linha[3]) + float(linha[4])
        if p1 > p2:
            nota_maxima = p1
            nota_minima = p2
        elif p2 > p1:
            nota_maxima = p2
            nota_minima = p1
        print('aluno '+ linha[0] + ' nota minima ', nota_minima ,' nota maxima ',nota_maxima)

for i, linha in enumerate(linhas):
    if linha[5] < 7:
        print('aluno '+ linha[0] + " pegou exame " )
