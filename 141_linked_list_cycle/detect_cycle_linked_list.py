
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def hasCycle(head):
        if not head or head.next == None:
            return False
        slow = head
        fast = slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


class TestDetectCycleLinkedList(object):
    def get_two_cycle(self):
        n1, n2 = ListNode(1), ListNode(2)
        n1.next = n2.next = n1
        return n1

    def get_simple_cycle(self):
        n1, n2, n3 = ListNode(1), ListNode(2), ListNode(3)
        n1.next = n2.next = n3.next = n1
        return n1

    def get_longer_no_cycle(self):
        n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
        n1.next = n2.next = n3.next = n4.next = n5
        return n1

    def test_detect_cycle_bad_input(self):
        assert not Solution.hasCycle(None)

    def test_detect_cycle_linked_list(self):
        head = self.get_two_cycle()
        assert Solution.hasCycle(head)
        head = self.get_simple_cycle()
        assert Solution.hasCycle(head)

    def test_detect_no_cycle_linked_list(self):
        assert not Solution.hasCycle(ListNode(1))
        head = ListNode(1).next = ListNode(2)
        assert not Solution.hasCycle(head)
        assert not Solution.hasCycle(self.get_longer_no_cycle())