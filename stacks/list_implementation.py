stack = []

#empty() operation
#use to check if the stack is empty
print(not bool(stack))

#push(element) operation
#append() function to push element in the stack
stack.append('1')
stack.append('2')
stack.append('3')
 
print('Initial stack')
print(stack)

#size() operation
#size of the stack
print('\nStack length')
print(len(stack))

#top() operation
#get the top of the stack
print('\nStack top element')
print(stack[-1]) #using backward indexing
print(stack[len(stack)-1])

#pop() operation
#pop() to pop element from stack in LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 
# uncommenting print(stack.pop()) will cause an IndexError as the stack is now empty
#print(stack.pop())
