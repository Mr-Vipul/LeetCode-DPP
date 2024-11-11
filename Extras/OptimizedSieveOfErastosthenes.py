N=19 
prime = [True]*(N+1)
prime[0] = prime[1] = False

for i in range(2, int(N**0.5)+1, 1):
    if prime[i] == True:
        for j in range(i*i, N+1, i):
            prime[j] = False 

print(prime)
        
            
    