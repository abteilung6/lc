import pytest


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_to_index: dict[int, int] = dict()
        for index, current_number in enumerate(nums):
            required_number = target - current_number
            maybe_index = number_to_index.get(required_number)
            if maybe_index is not None:
                return [maybe_index, index]
            number_to_index[current_number] = index
            



@pytest.mark.parametrize("nums,target,expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
    ([1, 1, 2, 3], 2, [0, 1]),
    ([1, 2], 3, [0, 1]),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, [8, 9]),
])
def test_two_sum(nums: list[int], target: int, expected: list[int]):
    solution = Solution()
    result = solution.twoSum(nums, target)
    assert result == expected
