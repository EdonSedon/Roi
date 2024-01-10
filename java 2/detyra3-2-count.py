lista = ["Hell", "world", "pershendejte"]
# lista = ["test","TT"]

def countWord(lista):
    newLista = []
    for fjala in lista:
        if len(fjala) >= 5:
            newLista.append(fjala)

    if not newLista:
        print("Lista skishte fjale me te gjate se 5 karaktere...")

    return newLista

print(countWord(lista))
