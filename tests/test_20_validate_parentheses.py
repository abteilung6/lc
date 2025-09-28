import pytest

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairs = {'()', '[]', '{}'}
        for char in s:
            if char in "([{":
                stack.append(char)
            elif not stack or stack.pop() + char not in valid_pairs:
                return False
        return not stack

@pytest.mark.parametrize("s,expected", [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([{}])", True),
    ("([{]})", False),
])
def test_isValid(s: str, expected: bool) -> None:
    solution = Solution()
    result = solution.isValid(s)
    assert result == expected
