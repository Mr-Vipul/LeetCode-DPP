# 1346. Check If N and Its Double Exist

def usingBinarySearch(arr):
    n = len(arr)
    
    for i in range(len(arr)):
        tar = 2*arr[i]
        right = len(arr)-1
        left = 0
        while(left<=right):
            mid = left + (right-left)//2
            if arr[mid] == tar and mid!=i:
                return True
            elif arr[mid] < tar:
                left = mid+1
            else:
                right = mid-1
    
    return False

arr = [0,0]
print(usingBinarySearch(arr))
    