
#Nome: Celso Zanquetta Junior
#ra: D76JCG-4
#Turma: CC5A41

import csv

def Geral():
    with open('Lista alunos.csv', 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            line[3] = (float(line[1]) + float(line[2]))
            line[6] = (float(line[4]) + float(line[5]))
            line[7] = (float(line[3]) + float(line[6]))/2
            if (float(line[7])>=7) and (float(line[7])<=10):
                print('Aluno: '+line[0]+'. \n Foi aprovado com media: '+ str(line[7]))
            else:
                print('Aluno: '+line[0]+'. \n Esta de exame com media: '+ str(line[7]))
                

def Aprovados():
    with open('Lista alunos.csv', 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            line[3] = (float(line[1]) + float(line[2]))
            line[6] = (float(line[4]) + float(line[5]))
            line[7] = (float(line[3]) + float(line[6]))/2
            if (float(line[7])>=7) and (float(line[7])<=10):
                print('Aluno: '+line[0]+'. \n Foi aprovado com media: '+ str(line[7]))
                
                

def MaiorNota():
    with open('Lista alunos.csv', 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        maior_nota = 0
        menor_nota = 0
        for line in csv_reader:
            line[3] = (float(line[1]) + float(line[2]))
            line[6] = (float(line[4]) + float(line[5]))
            line[7] = (float(line[3]) + float(line[6]))/2
            if (float(line[7])> maior_nota):
                maior_nota = float(line[7])
            elif((float(line[7])< menor_nota) or (menor_nota ==0)):
                menor_nota = float(line[7])
            
        print('A maior nota da turma foi: '+str(maior_nota))     
        print('A menor nota da turma foi: '+str(menor_nota))
            
            

def ListaDP():
    with open('Lista alunos.csv', 'r+') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        maior_nota = 0
        menor_nota = 0
        for line in csv_reader:
            line[3] = (float(line[1]) + float(line[2]))
            line[6] = (float(line[4]) + float(line[5]))
            line[7] = (float(line[3]) + float(line[6]))/2
            if (float(line[7])<=7) and (float(line[7])>=0):
                line[9] = (float(line[7]) + 0)/2
                if (float(line[9])<5) and (float(line[9])>=0):
                    print('Aluno: '+line[0]+'. \n Ficou de DP com media Final: '+ str(line[9]))
            
            

Geral()
print('\n\n')
Aprovados()
print('\n\n')
MaiorNota()
print('\n\n')
ListaDP()