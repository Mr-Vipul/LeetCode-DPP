class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        maxVal = max(nums)
        sieves = [True]*(maxVal+1)
        sieves[0]=sieves[1]=False

        for i in range(2, int(maxVal**0.5)+1):
            if sieves[i] == True:
                for j in range(i*i, maxVal+1, i):
                    sieves[j] = False 
        
        primes = []
        for i in range(2, maxVal+1):
            if sieves[i] == True:
                primes.append(i)
        
        # print(primes)

        prev = 0 
        for i in range(len(nums)):
            diff = nums[i] - prev - 1
        
            valid_prime = 0
            for prime in primes:
                if prime <= diff:
                    valid_prime = prime
                else:
                    break
            if valid_prime > 0:
                nums[i] -= valid_prime
            if nums[i] <= prev:
                return False
            prev = nums[i]

        return True
        
