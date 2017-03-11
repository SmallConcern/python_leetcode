import time

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed

def _gen_memo_key(open, closed):
    return "{}-{}".format(open, closed)

def _generate_parenthesis(substring, open, closed, memo):
    if not open and not closed:
        return []
    elif not open:
        return [substring + ')' * closed]
    options = []
    options += _generate_parenthesis(substring + '(', open - 1, closed, memo)
    if open < closed:
        options += _generate_parenthesis(substring + ')', open, closed-1, memo)
    return options

@timeit
def generate_parenthesis(n):
    memo = {}
    return _generate_parenthesis('', n, n, memo)

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
        generate_parenthesis(14)