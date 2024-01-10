def sumNr(numri):
    sum = 0
    for nr in range(numri):
        sum += nr 
    return sum
    

while True:
    numri = input("Sheno nje numer me te madh se 0 ose sheno (exit) per te perfunduar programin: ")
    if numri == 'exit':
        print("FLM")
        break
    
    if numri.isdigit() and int(numri) > 0:
        numri = int(numri)
        print(sumNr(numri))
    else:
        print("Sheno numrin me te madh se 0::")
