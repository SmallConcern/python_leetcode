
class Solution(object):
    def __init__(self):
        pass

    @staticmethod
    def twoSum(arr, n):
        n_complements = {}
        for idx, num in enumerate(arr):
            if num in n_complements:
                return [n_complements[num], idx]
            else:
                n_complements[n - num] = idx
        return [-1, -1]
