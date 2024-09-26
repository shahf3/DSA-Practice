def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = sorted(nums1 + nums2)
    
        n = len(mergedList)
    
        if n % 2 == 1:
            return mergedList[n // 2]
        else:
            mid1 = mergedList[n // 2 - 1]
            mid2 = mergedList[n // 2]
        return (mid1 + mid2) / 2
