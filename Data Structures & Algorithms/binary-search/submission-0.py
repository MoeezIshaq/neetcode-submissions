class Solution:
    def binary_search(self, l, h, target, nums):
        if l > h:
            return -1
        
        m = l + (h - l) // 2

        if target < nums[m]:
            return self.binary_search(l, m - 1, target, nums)
        elif target > nums[m]:
            return self.binary_search(m + 1, h, target, nums)
        else:
            return m

    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, target, nums)