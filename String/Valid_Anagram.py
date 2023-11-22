class Solution:
    def isAnagram(s: str, t: str) -> bool:
        chr_s = {}
        chr_t = {}

        for i in s :
            if i in chr_s: chr_s[i] += 1
            else : chr_s[i] = 0

        for j in t :
            if j in chr_t: chr_t[j] += 1
            else : chr_t[j] = 0

        check_chr = chr_s == chr_t
        if check_chr : return True
        
        return False





s,t = input("2 strings : ").split(" ")
print(Solution.isAnagram(s,t))