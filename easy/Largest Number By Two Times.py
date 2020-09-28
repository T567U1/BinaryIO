#Given a list of integers, return whether the largest number is bigger than the
#second-largest number by more than two times.
#For example, given the list [3, 9, 6], you should return false,
#since 9 is not bigger than 12 (2 times 6).
#Given the list [6, 3, 15], you should return true,
#since 15 is bigger than 12 (2 times 6).

# time complexity is o(n) either you sort or get the max still have to go through
# all elements on the array
class Solution:
    def solve(self, nums):
        # Write your code here
        if len(nums) < 2:
            return False
        nums.sort()
        return nums[-1] > nums[-2] * 2
