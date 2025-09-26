import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return x in (y, y // 10)


@pytest.mark.parametrize("x,expected", [
    (1221, True),     
    (-121, False),
    (10, False),
    (0, True),
    (12321, True),
])
def test_is_palindrome(x: int, expected: bool):
    solution = Solution()
    result = solution.isPalindrome(x)
    assert result == expected
