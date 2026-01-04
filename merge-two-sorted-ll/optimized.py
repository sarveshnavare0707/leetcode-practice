# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        prev = None # Store previous block reference

        if list1 and list2:

            curr = list1 # Store reference to head of the list 

            while list1 and list2:
                if list2.val >= list1.val:
                    prev = list1 # Set previous block value before moving forward
                    list1 = list1.next # move forward
                else:
                    temp = list1 # store the bigger element 
                    if prev:    
                        prev.next = ListNode(list2.val) # Insert smaller element
                        prev = prev.next # Update previous reference accordingly
                    else:
                        prev = ListNode(list2.val) # If inserting element at the beginning
                        curr = prev # Update head of list accordingly
                    prev.next = temp # Join the bigger element
                    list2 = list2.next # Move forward

            if list1:
                return curr
            else:
                while list2:
                    prev.next = ListNode(list2.val)
                    prev = prev.next
                    list2 = list2.next

            return curr
            
        elif list1:
            return list1
        else:
            return list2
    
if (__name__ == "__main__"):
    list1 = ListNode(2, ListNode(3, ListNode(4)))
    list2 = ListNode(1, ListNode(5))
    sol = Solution()
    newll = sol.mergeTwoLists(list1, list2)
    while newll:
        print(newll.val)
        newll = newll.next  # 1 2 3 4 5