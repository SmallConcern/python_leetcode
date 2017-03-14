def remove_duplicates(arr):
    if not arr:
        return 0
    swap_idx = 1
    for x in range(0, len(arr)):
        if arr[x] > arr[swap_idx-1]:
            arr[x], arr[swap_idx] = arr[swap_idx], arr[x]
            swap_idx += 1
    return swap_idx

class Solution(object):
    def removeDuplicates(self, nums):
        return remove_duplicates(nums)

class TestRemoveDuplicates(object):
    def test_remove_duplicates(self):
        nums = []
        assert remove_duplicates(nums) == 0
        assert nums == []
        nums = [1,1,2]
        assert remove_duplicates(nums) == 2
        assert nums == [1,2,1]
        nums = [1,1,2,2,3,4,5]
        assert remove_duplicates(nums) == 5
        assert nums[:5] == [1,2,3,4,5]
        nums = [1,2,3,4,5,6]
        assert remove_duplicates([1,2,3,4,5,6]) == 6
        assert nums == [1,2,3,4,5,6]
        nums = [1,1,1,1,1,1,1]
        assert remove_duplicates(nums) == 1
        assert nums[:1] == [1]
        nums = [1,1,1,1,1,1,1,2,3]
        assert remove_duplicates(nums) == 3
        assert nums[:3] == [1,2,3]