def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    open = []
    result = True
    long = len(s)

    if len(s) % 2 != 0 or s[0] not in ["(", "[","{"] or s[-1] not in [")", "]", "}"]:
        result = False
    elif (s.count("(") != s.count(")"))  or (s.count("{") != s.count("}")) or (s.count("[") != s.count("]")):
        result = False
    else:
        for i in range(0,long):
            if i == 0:
                open.append(s[i])
            elif s[i] in ["(", "[","{"]:
                open.append(s[i])
            else:
                if (open[-1] == "(" and s[i] == ")") or (open[-1] == "[" and s[i] == "]") or (open[-1] == "{" and s[i] == "}"):
                    open.pop()
                elif (open[-1] == "(" and s[i] != ")") or (open[-1] == "[" and s[i] != "]") or (open[-1] == "{" and s[i] != "}"):
                    result = False
                else:
                    pass

    return result
        



s = "[[[]"

result = isValid(s)

print(result)