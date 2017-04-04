class LetterCombos(object):
    def __init__(self):
        self.phone_num_map = {'1': '-', '2': 'abc', '3': 'def',
                              '4': 'ghi', '5': 'jkl', '6': 'mno',
                              '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
                              '0': '_'}

    def get_letter_combos(self, digit_string):
        combos = []
        if digit_string:
            self._get_possible_combos('', digit_string, 0, combos)
        return combos

    def _get_possible_combos(self, prefix, digit_string, start, combos):
        if start == len(digit_string):
            combos.append(prefix)
            return
        for letter in self.phone_num_map[digit_string[start]]:
            self._get_possible_combos(prefix + letter, digit_string, start + 1, combos)

class Solution(object):
    def letterCombinations(self, digits):
        lc = LetterCombos()
        return lc.get_letter_combos(digits)

class TestLetterCombos(object):
    def test_letter_combos(self):
        lc = LetterCombos()
        print lc.get_letter_combos('234')