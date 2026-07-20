class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Sort list
        nums.sort()
        
        # Return Kth LARGEST element
        return nums[len(nums) - k]