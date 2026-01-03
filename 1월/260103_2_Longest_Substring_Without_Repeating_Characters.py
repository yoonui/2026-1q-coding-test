def lengthOfLongestSubstring(s: str) -> int:
    str_dict = {}
    max_len = 0
    start = 0

    for end in range(len(s)):
        if s[end] in str_dict:
            start = max(start, str_dict[s[end]]+1)
        str_dict[s[end]] = end
        max_len = max(max_len, end-start+1)

    return max_len

# print(lengthOfLongestSubstring(" "))
print(lengthOfLongestSubstring("abba"))
# print(lengthOfLongestSubstring("bbbbb"))
# print(lengthOfLongestSubstring("abcabcbb"))