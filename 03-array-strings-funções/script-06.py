ar1 = [1,3,4,5,6,7]
ar2 = [3,4,65,7]

def removeSecond(arr1, arr2):
    arr3 = []
    for val1 in arr1:
        flag = 0
        
        for val2 in arr2:
            if val2 == val1:
                flag = 1

        if flag == 0:
            arr3.append(val1)

    return arr3

print(removeSecond(ar1, ar2))
