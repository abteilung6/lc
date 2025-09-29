from typing import Optional
import pytest

class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next
    
    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values) + " -> None"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next

@pytest.mark.parametrize("list1,list2,expected", [
    (
        ListNode(1, ListNode(2, ListNode(4))), 
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
    ),
])
def test_mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode], expected: Optional[ListNode]) -> None:
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    assert result == expected