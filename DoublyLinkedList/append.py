class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class doublyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
            return
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
            newNode.prev=curr
    def printList(self):
        curr=self.head
        while curr:
            print(curr.val,end="->")
            curr=curr.next
        print('None')
dll=doublyLinkedList()
dll.append(1)
dll.append(2)
dll.printList()