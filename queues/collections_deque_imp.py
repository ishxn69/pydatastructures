from collections import deque
 
#initialising a queue
q = deque()
 
#adding elements to a queue
q.append('1')
q.append('2')
q.append('3')
 
print("Initial queue")
print(q)
 
#removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
 
print("\nQueue after removing elements")
print(q)
 
#uncommenting q.popleft() will raise an IndexError as queue is now empty
q.popleft()
