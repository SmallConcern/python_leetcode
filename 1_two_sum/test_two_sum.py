from two_sum import TwoSum

class TestTwoSum():
    def test_find_two_sum_indices(self):
        arr = [2, 7, 11, 15]
        n = 9
        assert TwoSum.find_two_sum_indices(arr, n) == [0, 1]