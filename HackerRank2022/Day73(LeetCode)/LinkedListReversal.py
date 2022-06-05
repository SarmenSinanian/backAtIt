# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

input = [1,2,3,4,5]
output = [5,4,3,2,1]

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # initial heads new pointer aka end pointing to nothing
        if head:
            while head.next:  # head = 1 head.next = 2; head = 2 head.next = 3
                nextNode = head.next  # nextNode = 2;
                head.next = prev  # head.next (head's pointer) = None (prev);
                prev = head  # prev = 1;
                head = nextNode  # 2;
                # nextNode.next = prev
            head.next = prev

        return head