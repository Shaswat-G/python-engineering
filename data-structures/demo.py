items = [
    ("P1", 10),
    ("P2", 4),
    ("P3", 23),
    ("P4", 12),
    ("P5", 54),
    ("P6", 47),
    ("P7", 3),
    ("P8", 97),
    ("P9", 96),
    ("P10", 43),
]

filtered_items = filter(lambda x: x[1] > 20, items)
sorted_items = sorted(filtered_items, key=lambda x: x[1], reverse=True)
mapped_items = map(lambda x: (x[0], x[1] * 2), sorted_items)
print(list(mapped_items))


another_list = [1, 2, 4, 5, 1, 5, 3, 2, 9, 10]
print(list(zip(items, another_list)))


from collections import deque
queue = deque([1,2,3]) #wrap an empty list into the deque function to make it a queue.
print(queue)  # print the queue
queue.append(4) #add to the end of the queue
queue.append(5) #add to the end of the queue
queue.append(6) #add to the end of the queue
print(queue) #print the queue
queue.popleft() #remove from the front of the queue
queue.popleft() #remove from the front of the queue
print(queue) #print the queue

if not queue:
    print("Queue is empty")
    
    
    
    
    
from array import array
my_array = array("i", range(1000))
my_array.append(2)


from sys import getsizeof
values = (x**2 for x in range(1000))
print(values)
print(getsizeof(values)) # 112 bytes
