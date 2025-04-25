from collections import deque
stack = deque()

#pushing elements to stack
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print("Stack:",list(stack))

#to check if stack is empty
print("Is the stack empty? T/F", not bool(stack))

#to find the size of the stack
print("Size is",len(stack))

#to print the topmost element
print("Top is",stack[-1])

#to pop an element
print(stack[-1],"is popped")
stack.pop()
print("Stack:",list(stack))
