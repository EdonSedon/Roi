# (I)
list1 = [1, 2, 3, 4, 5, 6]
reversed = list1[::-1]
print(reversed)

# (II)

list1 = [1,2,3,4,5,6]
list1.reverse()
print(list1)


# This solution only changes the first matching number 20 ->2
list2 = [5,3,7,12,20,45,24,0,7,20]
if 20 in list2:
    list2[list2.index(20)] = 2

# This solution changes all the numbers 20 -> 2    
for i in range(len(list2)):
    if list2[i] == 20:
        list2[i] = 2
    

    
    




