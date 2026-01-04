# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        if list1 and list2:

            if list2.val >= list1.val:
                newll = ListNode(list1.val)
                list1 = list1.next
            else:
                newll = ListNode(list2.val)
                list2 = list2.next

            curr = newll

            while list1 and list2:
                if list2.val >= list1.val:
                    newll.next = ListNode(list1.val)
                    newll = newll.next
                    list1 = list1.next   
                else:
                    newll.next = ListNode(list2.val)
                    newll = newll.next
                    list2 = list2.next

            if list1:
                while list1:
                    newll.next = ListNode(list1.val)
                    newll = newll.next
                    list1 = list1.next
            else:
                while list2:
                    newll.next = ListNode(list2.val)
                    newll = newll.next
                    list2 = list2.next
            
            return curr

        elif list1:
            return list1
        else:
            return list2
    
if (__name__ == "__main__"):
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    sol = Solution()
    newll = sol.mergeTwoLists(list1, list2)
    while newll:
        print(newll.val)
        newll = newll.next  # 1 1 2 3 4 4
        