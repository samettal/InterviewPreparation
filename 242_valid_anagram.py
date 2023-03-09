# Solution 1:
# def isAnagram(s: str, t: str) -> bool:
#     dict1 = dict()
#     dict2 = dict()
    
#     for char in s:
#         if char not in dict1:
#             dict1[char] = 1
#         else:
#             dict1[char] += 1
#     print(dict1)
#     for char in t:
#         if char not in dict2:
#             dict2[char] = 1
#         else:
#             dict2[char] += 1
#     print(dict2)
#     if dict1 == dict2:
#         return True
#     else:
#         return False

# print(isAnagram('anagram','ranagma'))

# Solution 2:
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    hashmapS, hashmapT = dict(), dict()
    for i in range(len(s)):
        hashmapS[s[i]] = hashmapS.get(s[i], 0) + 1
        hashmapT[t[i]] = hashmapT.get(t[i], 0) + 1
    
    for c in hashmapS:
        if hashmapS[c] != hashmapT.get(c, 0):
            return False
    return True

print(isAnagram(s = 'anagram', t = 'managra'))