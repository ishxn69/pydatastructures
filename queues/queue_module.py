from queue import Queue
 
#initialising a queue
q = Queue(maxsize = 3)
 
#qsize() give the maxsize of the Queue
print(q.qsize())
 
#adding of element to queue
q.put(1)
q.put(2)
q.put(3)
 
#return Boolean for Full Queue
print("\nFull: ", q.full())
 
#removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
 
#return Boolean for Empty queue
print("\nEmpty: ", q.empty())
 
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
