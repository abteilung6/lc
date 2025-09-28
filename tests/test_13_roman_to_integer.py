import pytest


ROMAN_TO_INTEGER: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}



class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for index, current_char in enumerate(s):
            current_value = ROMAN_TO_INTEGER[current_char]
            if index == len(s) - 1:
                next_value = None
            else:
                next_char = s[index + 1]
                next_value = ROMAN_TO_INTEGER[next_char]
            if next_value is None or current_value >= next_value:
                result += current_value
            else:
                result -= current_value

        return result


@pytest.mark.parametrize("x,expected", [    
    ("III", 3),
    ("IV", 4),
    ("IX", 9),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
])
def test_romanToInt(x: str, expected: bool) -> None:
    solution = Solution()
    result = solution.romanToInt(x)
    assert result == expected
