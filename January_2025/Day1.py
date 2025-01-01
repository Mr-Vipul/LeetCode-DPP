def maxScore(s):
        zer = 0
        one = s.count("1")
        res = 0 

        for i in range(len(s)-1):
            if s[i]=="0":
                zer += 1
            else:
                one -= 1 
            res = max(res, zer+one)
        return res

s = "0111001"
print(maxScore(s))