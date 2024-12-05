def stringCheckNext(str, check):
    i = 0
    j = 0 
    
    while i<len(str) and j<len(check):
        if str[i] == check[j] or  (ord(str[i]) + 1 - ord('a'))%26 == ord(check[j]) - ord('a'):
            j+=1
        
        if j==len(check):
            return True 
        i+=1 
    
    return False


str = "za"
check = "ab"
print(stringCheckNext(str,check))