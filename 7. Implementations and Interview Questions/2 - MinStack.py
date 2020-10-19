class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, x):
        self.stack.append(x)
        
        if self.min:
            if x <= self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)
        
    def pop(self):
        if self.stack[-1] == self.min[-1]:
            self.min.pop()            
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min[-1]


## Example Execution ##
obj = MinStack()
obj.push(10)
obj.push(5)
obj.push(15)
obj.pop()
obj.push(20)

result_top = obj.top()
print("Top Value:", result_top)

result_min = obj.getMin()
print("Minimum Value in Stack:", result_min)