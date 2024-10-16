
#Approch for the climbe stairs:
def climb_stairs(n):#define climb_stairs:
    if n <= 1:
        return 1  
    
    
    dp = [0] * (n + 1)
    
    
    dp[0] = 1  
    dp[1] = 1  

    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  

    return dp[n]

if __name__ == "__main__":
    n = 2
    print(climb_stairs(n))  
# TIME COMPLEXCITY:
# BY BIG (O) NOTATION:
print("time complexcity will be O(n) ")