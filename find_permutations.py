/*
 * Given an array nums of distinct integers,
 * return all the possible permutations.
 */
# Solution 1: using default argument res
def permute(nums)
	res = []
	find(nums, [], res)
    return res
        
def find(nums, p, res=[]):
	if len(nums) == 0:
		res.append(p)
            
	for i in range(len(nums)):
		find(nums[:i] + nums[i+1:], p + [nums[i]], res)
        
# Solution 2: returning a list from each recursive call
def permute2(nums):
    return find2(nums, [])

def find2(nums, perm):
	if len(nums) == 0:
		return [perm]
	r = []
	for i in range(len(nums)):
		r += find2(nums[:i] + nums[i+1:], perm + [nums[i]])
		return r