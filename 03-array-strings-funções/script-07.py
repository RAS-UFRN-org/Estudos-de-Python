arr1 = [2,3,4,5,0,2,0,0,12]
arr2 = []

def moveZeroes(arr1, arr2):
    zeroCounter = 0
    for value in arr1:
        if value != 0:
            arr2.append(value)
        else:
            zeroCounter+= 1
    
    while zeroCounter != 0:
        zeroCounter -= 1
        arr2.append(0)

    return arr2

print(moveZeroes(arr1,arr2))
