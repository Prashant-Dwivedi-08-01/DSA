# Here we are asked to return minimum value using get_min() but with no extra space.
# Thus we can use only O(n) space here, viz. a variable to store the min value


class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.min_value = float('inf')

    def isStackEmpty(self):
        return len(self.stack) == 0

    def push(self, num):
        if self.isStackEmpty():
            self.stack.append(num)
            self.min_value = num
        elif num < self.min_value:
            self.stack.append(2*num - self.min_value)
            self.min_value = num
        else:
            self.stack.append(num)

    def pop(self):
        if not self.isStackEmpty():
            popped_value = self.stack.pop()
            if popped_value < self.min_value: #flag
                self.min_value = 2*self.min_value - popped_value
                return self.min_value
            else:
                return popped_value
    
    def get_min(self):
        return self.min_value

    def print_stack(self):
        for ele in reversed(self.stack):
            print("| " + str(ele) + " |")
            print(" --- ")
s = Stack()

s.push(23)
s.push(15)
s.push(6)
s.push(8)

s.print_stack()
print(s.get_min())

s.pop()
s.pop()
s.print_stack()
print(s.get_min())