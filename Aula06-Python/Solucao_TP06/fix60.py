
#Nome: Celso Zanquetta Junior
#ra: D76JCG-4
#Turma: CC5A41


text = ['Gol', 'Uno', 'Palio', 'EcoSport', 'Clio', 'Strada', 'Golf']

saveFile = open('fix60.txt', 'w')
for x in text:
    saveFile.write(x + "\n")
    
saveFile.close()


def Lista():
    saveFile = open('Lista.txt', 'w')
    for x in text:
        saveFile.write(x + "\n")
    
    saveFile.close()
    
def Reverso():
    saveFile = open('Reverso.txt', 'w')
    for x in reversed(text):
        saveFile.write(x+'\n')
        
    saveFile.close()
    
def Ordenado():
    text.sort()
    saveFile = open('Ordenado.txt', 'w')
    for x in text:
        saveFile.write(x + "\n")
        
    saveFile.close()
    
def Numerado():
    text.sort()
    saveFile = open('Numerado.txt', 'w')
    for number, x in enumerate(text, 1):
        saveFile.write(str(number) + ' - ' + x + "\n")
        
    saveFile.close()
    
Lista()
Reverso()
Ordenado()
Numerado()
