N=19 
prime = [True]*(N+1)
prime[0] = prime[1] = False

for i in range(2, N//2, 1):
    if prime[i] == True:
        for j in range(2*i, N+1, i):
            prime[j] = False 

print(prime)
        
            
    