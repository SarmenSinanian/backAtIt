# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Recursive

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        if list1 and list2:
            print(f'list1 = {list1} list2 = {list2}')
            if list1.val >= list2.val:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
            elif list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
        else:
            if list1:
                return list1
            if list2:
                return list2

# Iterative

class Solution:
    def mergeTwoListsIterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next