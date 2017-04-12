import sys

class Solution(object):
    def minSubArrayLen(self, s, nums):
        total, left = 0, 0
        min_size = len(nums) + 1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                min_size = min(min_size, right - left + 1)
                total -= nums[left]
                left += 1
        return min_size if min_size <= len(nums) else 0


class TestMaximumSubarray(object):
    def test_maximum_subarray(self):
        s = Solution()
        assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2