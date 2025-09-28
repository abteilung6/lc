import pytest


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        for scanning_index in range(len(strs[0])):
            for scanning_word in strs[1:]:
                if len(scanning_word) <= scanning_index or scanning_word[scanning_index] != strs[0][scanning_index]:
                    return strs[0][:scanning_index]
        return strs[0]

@pytest.mark.parametrize("strs,expected", [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["dog", "dog", "dog"], "dog"),
])
def test_longestCommonPrefix(strs: list[str], expected: str) -> None:
    solution = Solution()
    result = solution.longestCommonPrefix(strs)
    assert result == expected
