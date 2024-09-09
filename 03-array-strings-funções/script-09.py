arr1 = [2,3,4,5,6,7,8,9]
k = 2

def moveKAround(arr1: [int], k: int):
    arr2 = []
    for elem in range(k, arr1.__len__() + k):
        arr2.append(arr1[elem % arr1.__len__()])

    return arr2

print(moveKAround(arr1, k))
