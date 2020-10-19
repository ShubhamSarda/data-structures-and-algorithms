class MaxStack:
    
    def __init__(self):
        self.stack = []
        self.max = []
        
    def push(self, x):
        self.stack.append(x)
        
        if self.max:
            if x >= self.max[-1]:
                self.max.append(x)
        else:
            self.max.append(x)
        
    def pop(self):
        if self.stack[-1] == self.max[-1]:
            self.max.pop()            
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMax(self):
        return self.max[-1]


## Example Execution ##
obj = MaxStack()
obj.push(10)
obj.push(5)
obj.pop()
obj.push(20)
obj.push(15)

result_top = obj.top()
print("Top Value:", result_top)

result_max = obj.getMax()
print("Maximum Value in Stack:", result_max)