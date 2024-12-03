def stringSpaces(st,arr):
    
    ret = "" 
    prevIndex = 0 
    index = 0 
    for i in range(len(st)):
        if len(arr)>index  and i == arr[index]:
            ret += st[prevIndex:i] + " "    
            prevIndex = arr[index]
            index += 1 
            
    ret += st[arr[-1]:]
    return ret 
st = "LeetCodeTheLearning"
arr = [8,11]
print(stringSpaces(st,arr))