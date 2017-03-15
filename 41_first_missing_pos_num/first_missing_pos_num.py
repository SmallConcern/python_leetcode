class Solution(object):
    def firstMissingPositive(self, nums):
        for x in range(0, len(nums)):
            dest = nums[x]
            if dest-1 != x:
                while dest > 0 and dest <= len(nums):
                    if nums[x] == nums[dest - 1]:
                        break
                    else:
                        nums[x], nums[dest - 1] = nums[dest - 1], nums[x]
                        dest = nums[x]
        x = 0
        while x < len(nums):
            if nums[x] != x+1:
                break
            x += 1
        return x+1


class TestFirstMissingPosNum(object):
    def test_first_missing_pos_num(self):
        s = Solution()
        assert s.firstMissingPositive([]) == 1
        assert s.firstMissingPositive([1]) == 2
        assert s.firstMissingPositive([1, 1]) == 2
        assert s.firstMissingPositive([1, 2, 0]) == 3
        assert s.firstMissingPositive([3, 4, -1, 1]) == 2