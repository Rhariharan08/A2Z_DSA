# Problem Link -> https://leetcode.com/problems/rotate-array/
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l2 = nums[:-k]
        l1 = nums[-k:]
        for i in l2:
            l1.append(i)
        for i in range(0,len(l1)):
            nums[i] = l1[i]
