def lengthOfLongestSubstring(s):
    b = ''
    l = 0
    for i in s:
        if i in b:
            b = b[b.find(i) + 1:]
        b += i
        l = max(l, len(b))
    return l
print(lengthOfLongestSubstring('abcabcbb'))