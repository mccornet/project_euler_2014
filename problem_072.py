"""
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions 
for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set 
of reduced proper fractions for d ≤ 1,000,000?
"""

# Answer is sum of euler totient function for d = 1 to d = 10**6

def phi_sieve_1(N):

   # O(n) phi sieve
   MAXN = N
   phi = [0]*(MAXN+1)
   prime = [0]*(MAXN//10) # ONLY CORRECT FOR LARGE N, SMALLER N OUT OF RANGE ERRORS
   sz = 0
   mark = [0]*(MAXN+1)
   
   for i in range(2,MAXN+1):

      if(not mark[i]):
         phi[i] = i-1;
         prime[sz]= i;
         sz+=1

      j = 0
      while (j < sz and prime[j]*i <= MAXN):

         mark[prime[j]*i]=1

         if(i%prime[j]==0):

            phi[i*prime[j]] = phi[i]*prime[j]
            break
         
         else:
            phi[i*prime[j]] = phi[i]*(prime[j]-1 )
      
         j += 1

      # YIELD RESULT HERE
      #yield phi[i]

   # OR RETURN COMPLETE LIST HERE
   return phi


#res = sum(phi_sieve_1(1000000))
#print(res)
