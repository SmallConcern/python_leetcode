from median_sorted_arrays import Solution

class TestMedianSortedArrays():
    def test_median_sorted_arrays_simple(self):
        # arr1 = [1, 3]
        # arr2 = [2]
        # assert Solution.findMedianSortedArrays(arr1, arr2) == 2.0
        arr1 = [1, 2]
        arr2 = [3, 4]
        assert Solution.findMedianSortedArrays(arr1, arr2) == 2.5