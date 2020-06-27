# can partition in two equals arrays
def can_partition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # if sum(nums)&1 == 0:
    if sum(nums)%2 == 0:
        # target = sum(nums) >> 1
        target = sum(nums)//2
        cur = {0}
        for i in nums:
            cur |= {i + x for x in cur}
            #cur.update({i + x for x in cur})
            if target in cur:
                return True
    return False

#a = [1,2,3,5]
a = [1,5,11,5]
#a = [3,3,3,4,5]
#a=[80,38,97,19,81,96,70,35,12,44,33,51,78,86,31,74,94,54,11,91,7,90,83,12,91,67,40,80,39,87,17,49,66,56,15,99,95,91,22,49,14,23,18,74,22,62,14,94,75,97,45,32,9,21,14,70,93,14,91,6,99,12,29,32,26,33,44,24,82,84,95,10,91,38,23,27,64,88,83,85,7,23,62,49,60,67,31,55,87,42,61,4,7,10,12,8,94,9,30,59]
print(can_partition(a))































