class Solution(object):
    def countPrimes(n):
        prime = [True for _ in range(n+1)]
        for i in range(2,int((n**0.5))+1):
            if prime[i] == True:
                for j in range(i*i,n+1,i):
                    prime[j] = False

        prime_list = []
        for x in range(2, n+1):
            if prime[x]:
                prime_list.append(x)
        return prime_list


n = int(input("n = "))
prime = Solution.countPrimes(n)
print(prime)