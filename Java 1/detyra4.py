def gjejZanoret(fjalia) -> int:
    count = 0
    for char in fjalia.lower():
        if zanore(char):
            count +=1
    return count

def zanore(char):
    if char in ['a', 'e', 'i', 'o', 'u', 'y', 'ë']:
        return True
    return False

    # def zanore(char:)
        # return char in ['a', 'e', 'i', 'o', 'u', 'y']


fjalia = input('Shkruaj nje fjali qe permban zanore ose jo:')
print(f'Numri i zanoreve ne kete fjali eshte : {gjejZanoret(fjalia)}')
