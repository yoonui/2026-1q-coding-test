def longestPalindrome(s: str) -> str:
    def lookup(s, start, end):
        while start >=0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1:end]
    
    if len(s) <= 1 or s == s[::-1]: return s

    ans = ""
    for i in range(len(s)-1):
        ans = max(ans, lookup(s, i, i+1), lookup(s, i, i+2), key=len)
    return ans

# print(longestPalindrome("babad"))
# print(longestPalindrome("cbbd"))
# print(longestPalindrome("a"))
print(longestPalindrome("abcc"))