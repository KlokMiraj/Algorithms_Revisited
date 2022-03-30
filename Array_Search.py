# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
# (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
# You must decrease the overall operation steps as much as possible.
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        matching_index={}
        
        for i in range(len(nums)):
            matching_index[i]=nums[i]-target
            if(matching_index[i]==0):
                return True
        return False


def main():
    su=Solution()
    nums=[1,2,8,8,7,6,6,6,3,2]
    target=7
    print(nums)
    print(su.search(nums,target))

if __name__=="__main__":
    main()