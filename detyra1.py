
listaStudenteve = {
    'Albert': [8,7,9],
    'Xheni': [6,7,8],
    'Marta': [7,8,9],
    'Fatjon': [9,9,10],
    'Elton': [6,7,8],
    'Edon' : [10,10,10]
}

def llogaritMesataren(studentetNotat, mesataret):
    for emri, nota in studentetNotat.items():
        mesatare = sum(nota) / len(nota)
        mesataret[emri] = mesatare
        
        
#krijimi i nje dictionary per te ruajtur mesataren e secilit student
mesataret = {}

llogaritMesataren(listaStudenteve, mesataret)

print('----------------------')
print("Emri Studentit\tMesatarja")
print('----------------------')
for emri, mesatare in mesataret.items():
    print(f"{emri}\t\t{mesatare:.2f}")
