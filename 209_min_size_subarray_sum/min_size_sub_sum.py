class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """


class TestMaximumSubarray(object):
    def test_maximum_subarray(self):
        s = Solution()
        assert s.minSubArrayLen([2,3,1,2,4,3], 7) == 2