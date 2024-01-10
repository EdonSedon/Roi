nr = 13
prime = 'PRIME'
joPrime = "JO PRIME"

if nr == 1:
    print(f"Numri eshte (1) {joPrime}")
    
if nr > 1:
    for i in range(2, nr):
        if (nr % i) == 0:
            print(f'Numri i shtypur eshte {nr} dhe eshte: {joPrime}')
            break
    else:
        print(f'Numri i shtypur eshte {nr} dhe eshte: {prime}')
