# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, val):
        self.next = ListNode(val)

def reverse_linked_list_in_k_group(head):
    pass

class TestReverseNodesInKGroup(object):
    def string_to_linked_list(self, input):
        head = ListNode(None)
        next = head.next
        for c in input:
            if not head.val:
                head.val = c
                ne
            else:
                next.append(c)
                next = next.next
        return next


    def linked_list_to_string(self, head):
        output = ''
        while head:
            output += str(head.val)
            head = head.next
        return output

    def test_reverse_nodes(self):
        head = self.string_to_linked_list("12345")
        assert self.linked_list_to_string(head) == "12345"

