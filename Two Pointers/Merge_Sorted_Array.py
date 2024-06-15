# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1

        # Iterate backwards, comparing and placing elements in the correct position
        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in arr2, copy them
        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1

        # No need to copy arr1 elements, as they are already in place

        return arr1
        
