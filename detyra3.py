numrat = [6,5,88,100,13,8,7]

def mesatar(numrat):
    mesatarja = sum(numrat) / len(numrat)  
    return round(mesatarja,2)

print(f'Mesatarja aritmetike e rrumbullaksuar eshte : {mesatar(numrat)}')
    