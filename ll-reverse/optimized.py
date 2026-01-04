# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None # previous node of head

        while head:
            curr = head # store position of head in current node
            head = head.next # move head pointer ahead
            curr.next = prev # point next value of current node to previous node
            prev = curr # make previous node to current node

        return prev # return as head will be None

# Driver Code
if (__name__ == "__main__"):
    # Test Cases
    # 1->2->3->4->5->NULL
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Expected Output: 5->4->3->2->1->NULL
    sol = Solution()
    h = (sol.reverseList(head))
    while h!=None:
        print(h.val)
        h = h.next