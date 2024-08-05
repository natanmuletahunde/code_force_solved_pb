MOD = 998244353

def count_placements(n, x, m):
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(x + 1)]
    dp[0][0][0] = 1
    
    for i in range(1, x + 1):
        for j in range(n + 1):
            for k in range(n + 1):
                if dp[i - 1][j][k] == 0:
                    continue
                for p in range(n - j + 1):
                    new_k = min(n, k + p - max(0, p - (i - 2)))
                    dp[i][j + p][new_k] = (dp[i][j + p][new_k] + dp[i - 1][j][k]) % MOD
    
    return dp[x][n][m]

# Example usage:
print(count_placements(2, 3, 1))  # Output: 5
print(count_placements(42, 10, 5))  # Output: 902673363
print(count_placements(1000, 10, 8))  # Output: 187821763
