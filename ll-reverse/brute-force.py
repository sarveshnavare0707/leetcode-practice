# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        templist = [] # Temporary list to store all values of LL

        while head!=None: # Traverse LL
            templist.append(head.val)
            head = head.next

        if templist:
            templist = templist[::-1] # Reverse List

            newll = ListNode(templist[0]) # Make new LL with first element of reversed list
            curr = newll # Store the pointer to the head/start

            for t in range(1,len(templist)): # iterate from 1 to N
                newll.next = ListNode(templist[t]) # Attach next block to the next pointer
                newll = newll.next # Move pointer to the next block
            
            return curr

        else:

            return head

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