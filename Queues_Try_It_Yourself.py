""" Declare your queue here. Code wont work until you do this"""
# Code goes here

def enqueue(customer):
    """ Enqueue function. Using the append operation you can add to the queue.
        Allows you to input customers in the the Test case.
    """
    # Code goes here
        
def dequeue():
    """ Dequeue removes the first person that was enqueued. Using the .pop operator would be an easy
        solution.
    """
    # Code goes here
                    
# Test case(s)
print()
print("----------Test Case 1----------")
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