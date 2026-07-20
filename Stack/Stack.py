class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return "Stack is Empty"
        return self.items.pop()
    def size(self):
        return len(self.items)
    def top(self):
        if len(self.items)==0:
            return "stack is Empty"
        return self.items[-1]
stack=Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.items)
print(stack.pop())