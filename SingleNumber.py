class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        hashmaps = {}

        for num in nums:
            hashmaps[num] = hashmaps.get(num, 0) + 1
        
        for key, value in hashmaps.items():
            if  hashmaps[key] == 1:
                return key
        
        #print(hashmaps)