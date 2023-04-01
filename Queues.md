# Queues

## Introduction


You’re at your favorite amusement park, Disneyland, and you want to get on the rides as fast as you can. 
You narrow down the search criteria to one thing, which line is the shortest and you hop the long lines will get shorter after. 
You are utilizing the idea of a queue to help you achieve your goal!


![image](https://user-images.githubusercontent.com/108925950/229265999-85b7e4b5-044d-42b3-a1aa-8bcaaf87e381.png)

# How queues work

Queues are pretty straight forward and we use them all the time. 
A queue is referred to as First In First Out (FIFO) or a different way of saying it is Last In Last Out (LILO). 
This means that the first person in line is going to be the first one out like a grocery store line or my example above, a line at Disneyland. 
A queue has a lot of uses and functionality in programming.

![image](https://user-images.githubusercontent.com/108925950/229266069-45db0927-54ca-4258-a920-d9a73db595cb.png)


To represent the idea further another example of this is if you’re driving a car and come to a stop sign. 
You are in a line and (if everyone is a good driver you) the order of drivers will stay the same until each person goes 
through the intersection where the stop sign is.

![image](https://user-images.githubusercontent.com/108925950/229266092-3f95622e-f56d-4b94-aed3-4ba4d0ad90ef.png)


For the examples, we will stick to the original idea of the line at Disneyland. 
The lines work exactly like the car example. There’s even an invisible stop sign when you have to wait for the 
next rollercoaster car to pick up the next people.

# Operations/ Performance

Queues are very important for many programs and they have great performance. Typically queues have an O(1) performance which is one of the best performances we can have. There are many operations a queue has that I have outlined below.


## Enqueue:
The enqueue operation allows you to add onto the back of the queue (Crazy right!)  “Wild” - My roommate. This comes into play when someone in Disneyland park walks into the back of the line for the coaster, that person is “enqueued” into the line.

#### Python:

queue.enqueue()

## Dequeue:
The Dequeue operation allows you to remove the person that was first in line. In other word’s the person in the front of the line at Disneyland is the one that gets “dequeued” when he or she gets on the coaster to ride. (How fun!)

#### Python:

queue.dequeue()

## isEmpty:
This operator looks at the queue to see if it is empty. I choose isEmpty because of my scenario about the coaster. If the line is empty them logically it would not be worth running the coaster. That being said, we will check for if the queue is empty.


Other notable operators are: front, back, isFull, size and so on

Why not just use a list? Because lists are not time efficient for this purpose of first in first out scenario.

# Code example

This is one example of how you could make a queue using .put and .get

![Queue_Example_Code](https://user-images.githubusercontent.com/108925950/229269510-3ddc2cc3-5f88-483d-9bfc-5b2e3e05cc1e.jpg)



# Try it yourself!

Try it yourself! Below is a little problem I made up so you could test your knowledge. All you have to do is write the code inside the fuctions for a queue. Only two things need to work, enqueue and dequeue. You can do it!! Get the code here: [Try it yourself]([
](https://github.com/Cartman3/Data_Structures_Tutorial/blob/main/Queues_Try_It_Yourself.py))

![Queues_Try_Me](https://user-images.githubusercontent.com/108925950/229268473-c81798c6-1864-49f2-bccd-c42281235cd4.jpg)



Here is a link to one (of many) solutions to the problem: [Solution](https://github.com/Cartman3/Data_Structures_Tutorial/blob/main/Queues_Try_It_Yourself_solution.py)
