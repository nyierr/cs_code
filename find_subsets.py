/*
 * Given an integer array nums of unique elements,
 * return all possible subsets. Duplicates allowed.
 */
def subsets(self, nums):
    res = []
    find(sorted(nums), [], res)
    return res

def find(self, nums, sub, res=[]):
    res.append(sub)
    for i in range(len(nums)):
        self.helper(nums[:i] + nums[i+1:], sub + [nums[i]], res)
        
/*
 * Given an integer array nums of unique elements,
 * return all possible subsets. Duplicates NOT allowed.
 */
def uniqueSubsets(self, nums):
    res = []
    findUnique(sorted(nums), [], res)
    return res

def findUnique(self, nums, sub, res=[]):
    res.append(sub)
    for i in range(len(nums)):
        self.helper(nums[i+1:], sub + [nums[i]], res)
        
#
# Finding non-unique subsets
# --------------------------
# Recursion tree to find all non-unique subsets for nums=[1,2,3]:
#
# s=[], nums = [1,2,3]
#  + x = 1, s=[1], nums = [2,3]
#     + x = 2, s=[1,2], nums = [3]
#        + x = 3, s=[1,2,3], nums = []
#     + x = 3, s=[1,3], nums = [2]
#        + x = 2, s=[1,3,2], nums = []
#       
#  + x = 2, s=[2], nums = [1,3]
#     + x = 1, s=[2,1], nums = [3]
#        + x = 3, s=[2,1,3], nums = []
#     + x = 3, s=[2,3], nums = [1]
#        + x = 1, s=[2,3,1], nums = []
#       
#  + x = 3, s=[3], nums = [1,2]
#     + x = 1, s=[3,1], nums = [2]
#        + x = 2, s=[3,1,2], nums = []
#     + x = 2, s=[3,2], nums = [1]
#        + x = 1, s=[3,2,1], nums = []
#
# We follow the depth-first approach to generate all subsets.
# We start at the root level with s = []. Then we take a value from
# nums, append it to s and repeat the process (with updated s) until
# nums gets empty (e.g. [] -> [1] -> [1,2] -> [1,2,3])
#  
#
# Finding unique subsets
# --------------------------
# If we have a look at the above recursion tree, we can notice that
# by the time we start descending the branch with s=[3] and nums[1,2],
# we are already aware of the majority of its subsets:
#   - [3,1] is the same as [1,3] 
#   - [3,2] is the same as [2,3]
#   - [3,1,2] and [3,2,1] are the same as [1,2,3]
# The only new subset we get here is [3].
# Similary:
#   -for s=[2], nums = [1,3], the only new subsets are [2] and [2,3]
#   -for s=[1], nums = [2,3], all subsets are new except of [1,3,2]
# So to avoid duplicates, nums should only contain values greater
# than x (as opposed to all values except of x).

# Our recursion tree then looks like this:
# s=[], nums = [1,2,3]
#  + x = 1, s=[1], nums = [2,3]
#     + x = 2, s=[1,2], nums = [3]
#        + x = 3, s=[1,2,3], nums = []
#     + x = 3, s=[1,3], nums = []
#       
#  + x = 2, s=[2], nums = [3]
#     + x = 3, s=[2,3], nums = [] 
#       
#  + x = 3, s=[3], nums = []

