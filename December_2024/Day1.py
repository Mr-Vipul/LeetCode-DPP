# 1346. Check If N and Its Double Exist

def usingBinarySearch(arr):
    n = len(arr)
    """Time Complexity is O(n*logn)
       Space Complexity is O(1)"""
    arr.sort()
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


def usingHashSet(arr):
    """ T.C is O(n)
        S.C is O(n) """
    seen = set()
    for n in arr:
        if 2*n in seen or n//2 in seen:
            return True 
        seen.add(n)
    return  False
    

arr = [0,0]
print("Using Binary Search ->",usingBinarySearch(arr))
print("Using HashSet ->",usingHashSet(arr))
    