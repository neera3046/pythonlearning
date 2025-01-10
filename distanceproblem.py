def minDistance(s1: str, s2: str) -> int:
    m, n = len(s1), len(s2)
    # Initialize a 2D DP array
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case initialization
    for i in range(m + 1):
        dp[i][0] = i  # If s2 is empty, we need to remove all characters of s1
    for j in range(n + 1):
        dp[0][j] = j  # If s1 is empty, we need to insert all characters of s2

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no extra operation needed
            else:
                dp[i][j] = min(dp[i - 1][j],      # Remove operation
                               dp[i][j - 1],      # Insert operation
                               dp[i - 1][j - 1]   # Replace operation
                              ) + 1

    # The answer is in the cell dp[m][n]
    return dp[m][n]

# Example usage:
s1 = "neeraj"
s2 = "keerav"
print(minDistance(s1, s2))  # Output: 3
