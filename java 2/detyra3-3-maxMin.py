def maxMin(numbers):
    max = 0
    min = numbers[0]
    
    for num in numbers:
        if num > max:
            max = num
        if num < min:
            min = num
        
    return [max, min]
    
numbers = [10, 20, 30, 5, 100, 7, 33,2]
print(maxMin(numbers))

print("Metoda e dyte")
maxAndMin = [max(numbers),min(numbers)]
print(f'Max: {maxAndMin[0]}, Min: {maxAndMin[1]}')


