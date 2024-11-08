# 1829. Maximum XOR for Each Query
def getMaximumXor(nums,maxBits):
    pre = [nums[0]]
    
    for i in range(1,len(nums)):
        pre.append(nums[i]^pre[-1])
    
    ans = []
    k = 2**maxBits - 1
    
    for i in range(len(nums)-1,-1,-1):
        ans.append(pre[i]^(k)) 
    
    return ans 

nums = [0,1,1,3]
print(getMaximumXor(nums,2))
    
    