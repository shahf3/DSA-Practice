def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmaps = {}

        for key, value in enumerate(nums):
            difference = target - value

            if difference in hashmaps:
                return [hashmaps[difference], key]
            
            hashmaps[value] = key