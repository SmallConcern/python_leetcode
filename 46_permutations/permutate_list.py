import itertools

def permutations(sub_list, input_list, permutes):
    if len(input_list) == 0:
        permutes.append(sub_list)
    else:
        for idx, num in enumerate(input_list):
            permutations(sub_list + [num], input_list[:idx] + input_list[idx+1:], permutes)

def list_permutations(input_list):
    permutes = []
    prefix = []
    permutations(prefix, input_list, permutes)
    return permutes

class Solution(object):
    @staticmethod
    def python_permute(nums):
        perms = [list(perm) for perm in itertools.permutations(nums)]
        return perms

    @staticmethod
    def permute(nums):
        return list_permutations(nums)

class TestListPermutations(object):
    def test_list_permutations(self):
        assert Solution.permute([1,2,3]) == Solution.python_permute([1,2,3])