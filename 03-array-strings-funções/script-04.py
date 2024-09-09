array = [1,6564,4,564,564 ,654, 64, 64]
num = 64

def countTimes(array, num) -> int:
    count = 0
    for elem in array:
        if elem == num:
            count += 1

    return count

print(countTimes(array, num))
