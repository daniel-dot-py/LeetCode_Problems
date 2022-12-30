
def twoSum(nums, target):
    solucion = []
    contador = 0
    long = len(nums) - 1

    for i in nums[:long]:
        contador = contador + 1
        for j in nums[contador:]:
            if (i + j) == target:
                solucion.append(nums.index(i))
                solucion.append(nums[contador:].index(j)+contador)
                break
            else:
                pass
    return solucion





nums = [3,2,4]
target = 6

solucion = twoSum(nums,target)
print(solucion)
