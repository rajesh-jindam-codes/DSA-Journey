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
    def printList(self):
            temp=self.head
            while temp:
                print(temp.val,end="->")
                temp=temp.next
            print('None')
    def addTwoNumbers(self,l1,l2):
        dummy=Node(0)
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0
            total=x+y+carry
            carry=total//10
            curr.next=Node(total%10)
            curr=curr.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
sll1=singlyLinkedList()
sll1.append(2)
sll1.append(4)
sll1.append(3)
# sll1.append(40)
# sll1.append(50)
sll1.printList()

sll2=singlyLinkedList()
sll2.append(5)
sll2.append(6)
sll2.append(4)
# sll2.append(31)
# sll2.append(13)
sll2.printList()
result=sll1.addTwoNumbers(sll1.head,sll2.head)
temp=result
while temp:
    print(temp.val,end='->')
    temp=temp.next
print("None")