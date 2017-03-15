def remove_num(arr, num):
    purgatory = len(arr)-1
    for x in range(0, len(arr)):
        while purgatory > 0 and arr[purgatory] == num:
            purgatory -= 1
        if arr[x] == num:
            arr[x], arr[purgatory] = arr[purgatory], arr[x]
        if x == purgatory:
            break
    return purgatory

class Solution(object):
    def removeElement(self, nums, val):
        return remove_num(nums, val)

class TestRemoveDuplicates(object):
    def test_remove_duplicates(self):
        nums = [1, 1, 3, 3, 2, 2, 3, 6]
        size = remove_num(nums, 3)
        assert nums[:size] == [1,1,6,2,2]
        nums = [1, 2, 4, 5, 6]
        size = remove_num(nums, 3)
        assert nums[:size] == [1,2,4,5,6]
        nums = [3]
        size = remove_num(nums, 3)
        assert nums[:size] == []
        nums = [3,2,2,3]
        size = remove_num(nums, 3)
        assert nums[:size] == [2,2]
        nums = [2,2,3]
        size = remove_num(nums, 2)
        assert nums[:size] == [3]