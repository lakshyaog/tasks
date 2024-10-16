class ListNode:# DEFINE NODE :
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    if not head:
        return None

    slow = head
    fast = head

    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        
        if slow == fast:
            # To find the entry point of the cycle
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
            return entry  

    return None   

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  

    cycle_node = detectCycle(head)
    
    if cycle_node:
        print("Cycle detected at node with value:", cycle_node.val)
    else:
        print("No cycle detected")
# Time complexcity:
print("time complexcity of the code is O()n")