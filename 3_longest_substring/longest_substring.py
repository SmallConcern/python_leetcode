class LongestSubstring(object):
    def __init__(self):
        pass

    @staticmethod
    def find_longest_substring(input_str):
        char_dict = {}
        start, max_length = 0, 0
        for idx, char in enumerate(input_str):
            if char in char_dict and start <= char_dict[char]:
                start = char_dict[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)
            char_dict[char] = idx
        return max_length


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        return LongestSubstring.find_longest_substring(s)
