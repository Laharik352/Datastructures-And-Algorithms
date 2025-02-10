def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    r = []
    N = len(nums)
    for i in range(N):
        for j in range(i + 1, N):
            if nums[i] + nums[j] == target:
                r.append([nums[i], nums[j]])
    return r
print(twoSum([1,3,2,2],4))
print(twoSum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10))


# def subpairs(nums):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     s = []
#     r = set()
#     N = len(nums)
#     for i in range(N):
#         for j in range(i + 1, N):
#             s.append(sorted([nums[i], nums[j]]))
#     r = set(s)
#     return r
# print(subpairs([1,3,2,2]))
# print(subpairs([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1]))