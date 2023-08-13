def lcs(s1,s2):
        x = len(s1)
        y = len(s2)
        
        dp=[[None]*(x+1) for i in range(y+1)] # len = 7
        for i in range(y+1):
            for j in range(x+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif s2[i-1]==s1[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                    
        # print(dp)
        return dp[6][6]

print(lcs("ABCDGH","AEDFHR"))
