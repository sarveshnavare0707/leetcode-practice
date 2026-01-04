# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:

        hashmap = {} #hashmap to store the count of each node
        hashmap["default"] = 1 # as I am using set to check if all values are same, I need to have a default value in hashmap

        while True:
            if head and (len(set(hashmap.values()))==1): # loop until head is not None and all values in hashmap are same ie 1
                if hashmap.get(head):
                    hashmap[head] += 1
                else:
                    hashmap[head] = 1
                head = head.next
            else:
                break
                
        if len(set(hashmap.values()))!=1: # check if all values in hashmap are same ie 1
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
        