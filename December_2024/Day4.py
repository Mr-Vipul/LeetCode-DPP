def stringCheckNext(str, check):
    i = 0
    j = 0 
    
    while i<len(str) and j<len(check):
        if str[i] == check[j] or chr(ord(str[i])+1)%26==check[j]:
            j+=1
        
        if j==len(check):
            return True 
        i+=1 
    
    return False


str = "zb"
check = "ac"
print(stringCheckNext(str,check))