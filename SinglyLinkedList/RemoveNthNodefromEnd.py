class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class singlyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head is None:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    def deleteNthNode(self, n):
        fast = self.head
        slow = self.head

    # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

    # If we need to delete the head node
        if fast is None:
            self.head = self.head.next
            return self.head

    # Move both pointers until fast reaches the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

    # Delete the nth node from the end
        slow.next = slow.next.next

        return self.head
    def printList(self):
        temp=self.head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print('None')
sll=singlyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.printList()
sll.deleteNthNode(1)
sll.printList()
# sll.deleteNthNode(1)
