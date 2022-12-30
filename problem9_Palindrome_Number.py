def isPalindrome(x):
    x1 = str(x)
    print(x1)
    y = x1[::-1]
    print(y)
    solution = x1 == y
    return solution

solution = isPalindrome(-121)

print(solution)
