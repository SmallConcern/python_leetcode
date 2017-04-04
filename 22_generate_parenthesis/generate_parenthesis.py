def _generate_parenthesis(substring, open, closed):
    if not open and not closed:
        return []
    elif not open:
        return [substring + ')' * closed]
    options = []
    options += _generate_parenthesis(substring + '(', open - 1, closed)
    if open < closed:
        options += _generate_parenthesis(substring + ')', open, closed-1)
    return options

def generate_parenthesis(n):
    return _generate_parenthesis('', n, n)

class Solution(object):
    def generateParenthesis(self, n):
        return generate_parenthesis(n)


class TestGenParenthesis(object):
    def test_generate_parenthesis(self):
        assert generate_parenthesis(0) == []
        print generate_parenthesis(3)
        assert generate_parenthesis(3) == [
                                          "((()))",
                                          "(()())",
                                          "(())()",
                                          "()(())",
                                          "()()()"
                                          ]
        print generate_parenthesis(14)