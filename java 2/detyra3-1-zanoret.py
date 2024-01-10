def removeWowels(lista):
    vowels = "aeiouy"
    newList = []

    for word in lista:
        newWord = ''
        word = word.lower()
        for char in word:
            if char not in vowels:
                newWord += char
        newList.append(newWord)

    return newList

input_list = ["Pershendetje", "ROI"]
listaRe = removeWowels(input_list)

print("Input list:", input_list)
print("Output list without vowels:", listaRe)
