# Isso só é pra funcionar pra números positivos
arr1 = [4,1,2,3,4,5,6,7,8,9,10]
target = 8

def findTarget(arr: list, target):
    output = []
    arr.sort() 
    ii = 0
    jj = len(arr) - 1
    while ii < jj:
        currentResult = arr[ii] + arr[jj]
        if currentResult == target:
            output.append((arr[ii], arr[jj]))
            ii+=1
        elif currentResult < target:
            ii+= 1
        elif currentResult > target:
            jj -= 1
    return output

print(findTarget(arr1, target))
