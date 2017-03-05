from two_sum import Solution

class TestSolution():
    def test_find_two_sum_indices(self):
        assert Solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
        assert Solution.twoSum([2, 7, 11, 15], 15) == [-1, -1]
        assert Solution.twoSum([-1, 3], 2) == [0, 1]
        assert Solution.twoSum([1, 2, 3, 4, 5, -10], -5) == [4, 5]
        assert Solution.twoSum([3, 1, 2, -3], 0) == [0, 3]