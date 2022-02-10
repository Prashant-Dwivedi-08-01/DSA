# Push, Pop and getMin() functions to be implemented
# getMin() should be O(1)

class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = []

    def isStackEmpty(self):
        return len(self.stack) == 0

    def isMinStackEmpty(self):
        return len(self.minStack) == 0

    def push(self, num):
        self.stack.append(num)
        if self.isMinStackEmpty():
            self.minStack.append(num)
        elif self.minStack[len(self.minStack) -1] >= num:
            self.minStack.append(num)
    
    def pop(self):
        if not self.isStackEmpty():
            popped_value = self.stack.pop()
            if not self.isMinStackEmpty() and self.minStack[len(self.minStack) -1] == popped_value:
                self.minStack.pop()
    
    def get_min(self):
        if not self.isMinStackEmpty():
            return self.minStack[len(self.minStack) -1]
    def print_stack(self):
        for ele in reversed(self.stack):
            print("| " + str(ele) + " |")
            print(" --- ")
s = Stack()

s.push(10)
s.push(5)
s.push(30)

s.print_stack()

print(s.get_min())

s.pop()
s.print_stack()
print(s.get_min())

s.pop()
s.print_stack()
print(s.get_min())

s.push(6)
s.print_stack()
print(s.get_min())