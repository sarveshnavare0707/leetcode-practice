# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        if head.next!=None and head.next.next==head: # check if next of head is pointing to head
            return True
        elif head.next==None: # check if head is the only node
            return False
        elif head.next==head: # check if head is the only node and pointing to itself
            return True
        else:
            ptr1 = head # points at head
            ptr2 = head.next # points at next of head
            while ptr2 and ptr1!=ptr2: # loop until ptr2 reaches end of list or ptr1 and ptr2 meet
                ptr1 = ptr1.next # move ptr1 by 1
                ptr2 = ptr2.next # move ptr2 by 2 but 1 by 1 to avoid Nonetype error
                if ptr2!=None:
                    ptr2 = ptr2.next
            if ptr1==ptr2:
                return True
            else:
                return False

if __name__ == "__main__":
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(s.hasCycle(head))

    headnew = ListNode(1)
    headnew.next = ListNode(2)
    print(s.hasCycle(headnew))

        