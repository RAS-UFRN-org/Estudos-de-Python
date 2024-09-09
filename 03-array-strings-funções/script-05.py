arr = [1,2,3,4,4,5,6,7,8]
maps = {}
finArr = []

for elem in arr:
    if maps.get(elem) is None:
        maps[elem] = True
        finArr.append(elem)
    

print(maps)
print(finArr)

    
