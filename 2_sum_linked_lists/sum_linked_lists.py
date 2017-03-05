class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.root = None

    def append(self, num):
        current_node = self.root
        if not current_node:
            self.root = ListNode(num)
        else:
            while current_node.next:
                current_node = current_node.next
            current_node.next = ListNode(num)

    @staticmethod
    def add_two_linked_lists(l1, l2):
        n1 = LinkedList.linked_list_to_reversed_num(l1)
        n2 = LinkedList.linked_list_to_reversed_num(l2)
        return LinkedList.linked_list_from_str(str(n1 + n2)[::-1])

    @staticmethod
    def linked_list_from_num(num):
        num_str = str(num)
        ll = LinkedList()
        for num in num_str:
            ll.append(int(num))
        return ll

    @staticmethod
    def linked_list_from_str(input_str):
        ll = LinkedList()
        for char in input_str:
            ll.append(int(char))
        return ll

    @staticmethod
    def linked_list_to_reversed_num(linked_list):
        list_str = LinkedList.linked_list_to_str(linked_list)
        return int(list_str[::-1])

    @staticmethod
    def linked_list_to_str(linked_list):
        output_str = ''
        current_node = linked_list.root
        while current_node:
            output_str += str(current_node.val)
            current_node = current_node.next
        return output_str


class Solution(object):
    def __init__(self):
        pass

    @staticmethod
    def addTwoNumbers(l1, l2):
        ll_1, ll_2 = LinkedList(), LinkedList()
        ll_1.root = l1
        ll_2.root = l2
        return LinkedList.add_two_linked_lists(ll_1, ll_2).root