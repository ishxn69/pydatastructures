from queue import LifoQueue
 
# Initializing a stack
stack = LifoQueue(maxsize=3)
 
#qsize() show the number of elements in the stack
print(stack.qsize())
 
# put() function to push element in the stack
stack.put(1)
stack.put(2)
stack.put(3)
 
print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() function to pop element from stack in LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
 
print("\nEmpty: ", stack.empty())
