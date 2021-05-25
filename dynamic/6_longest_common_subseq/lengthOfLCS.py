def lengthOfLCS(str1, str2):
    return helper(str1, str2, len(str1) , len(str2))

def helper(str1, str2, m, n):
    if n == 0 or m == 0:
        result = 0
    elif str1[m - 1] == str2[n - 1]:
        result = 1 + helper(str1, str2, m - 1, n - 1)
    elif str1[m - 1] != str2[n - 1]:
        tmp1 = helper(str1, str2, m - 1, n)
        tmp2 = helper(str1, str2, m , n - 1)
        result = max(tmp1, tmp2)
    return result

# Better 
def lengthOfLCS(str1, str2):
    lcs = [[0 for x in range(len(str1) + 1)]for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str1[j - 1] == str2[i - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
    return lcs[-1][-1]

str1 = "abc"
str2 = "ac"
print(lengthOfLCS(str1, str2))
