def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) < 1:
        return ""
    
    long = min(strs, key= len)



    for i, char in enumerate(long):
        for other in strs:
            if other[i] != char:
                long = long[:i]
                break
    
    return long



strs = ["flower","flow","flight"]

done = longestCommonPrefix(strs)

print(done)
