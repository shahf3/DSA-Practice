class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            midL = (left + right) // 2

            if nums[midL] == target:
                return midL
            
            elif nums[midL] < target:
                left = midL + 1
            else:
                right = midL - 1
        return -1