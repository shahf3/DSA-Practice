class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmaps = {}

        for num in nums:
            hashmaps[num] = hashmaps.get(num, 0) + 1

        #print(hashmaps)

        for k, v in hashmaps.items():
            if hashmaps[k] > (len(nums) / 2):
                return k