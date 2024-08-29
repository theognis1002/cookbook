class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
        self.val = val
        self.next = next


class Solution:
    def has_cycle(self, head: ListNode | None) -> bool:
        fast = head

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False
