queue = []

def enqueue(customer):
    queue.append(customer)
    
    return queue
        
def dequeue():
    if len(queue) != 0:
            queue.pop(0)
    return queue
                    
# Test cases
print()
print("----------Test 1----------")
print()
enqueue('Parker')
enqueue('Zack')
enqueue('Carter')
print(queue) # "Parker", "Zack", "Carter"
dequeue() # Dequeues the first in which would be Parker
print()
print(queue) # "Zack", "Carter"
enqueue('Bob')
print()
print(queue) # Test if it enqueued after dequeued
print()
dequeue()
print(queue) # Final test to see if it still dequeues the first in
print()