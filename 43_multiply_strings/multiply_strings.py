

def multiply_strings(n1, n2):
    multiply_results = []
    for bottom_idx, bottom_digit in enumerate(reversed(n1)):
        carry = 0
        new_result = 0
        for top_idx, top_digit in enumerate(reversed(n2)):
            result = (int(top_digit) * int(bottom_digit)) + carry
            carry = result / 10
            new_result += 10**top_idx * (result % 10) if top_idx > 0 else result % 10
        if carry:
            new_result += 10**len(n2) * carry
        if bottom_idx > 0:
            new_result = new_result * 10**bottom_idx
        multiply_results.append(new_result)

    return sum(multiply_results)


class Solution(object):
    def multiply(self, num1, num2):
        return str(multiply_strings(num1, num2))


class TestMultiplyStrings(object):
    def test_multiply_strings(self):
        assert multiply_strings("6", "7") == 42
        assert multiply_strings("16", "7") == 112
        assert multiply_strings("1", "999") == 999
        assert multiply_strings("12345", "6789") == 83810205
        assert multiply_strings("6789", "12345") == 83810205