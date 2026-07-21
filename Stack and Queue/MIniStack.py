class MinStack:
    def __init__(self):
        self.stack=[]
    def push(self,val):
        if len(self.stack)==0:
            self.stack.append([val,val])
        else:
            currMin=self.stack[-1][1]
            newMin=min(currMin,val)
            self.stack.append([val,newMin])
    def pop(self):
        if self.stack:
            self.stack.pop()
    def top(self):
        if not self.stack:
            return None
        else:
            return self.stack[-1][0]
    def getMin(self):
        if not self.stack:
            return False
        return self.stack[-1][1]
ms=MinStack()
ms.push(1)
ms.push(-1)
ms.push(0)
print(ms.getMin())