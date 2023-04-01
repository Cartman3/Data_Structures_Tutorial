# Set

## Introduction

Let’s say you own a valet business and have 100’s of employees. You’re entering in driver’s license numbers of all your employees into a big spread sheet 
but you don’t want duplicates. An accident happens and you mix up all the drivers licenses. Now you don’t know which ones you entered and which ones you 
didn’t. This is where a set would come in real handy. It will still be a pain but the set will only keep one of each unique number.

## How does a set work?

A set has two important characteristics to them. One, the order is not important. Two, a set does not allow for duplicates. So sets arent to appealing if you care about the order. However, in the cases you dont then sets are wonderful. If youre worried about not having duplicates then sets are great for you! Another example of this is a deck of playing cards if you are playing a game that involves ONE deck. This is excatly a set in a way because although they have more than one number, you have different suits so there isnt really any duplication here. You also would shuffle the cards so order would not matter in this situation either.

![Sets_Intro](https://user-images.githubusercontent.com/108925950/229270423-df53b4ad-0239-4f30-adfd-904f22e5508f.jpg)

This example can be good to think about for the over all idea of a set. However, a set involves a more in depth concept to grasp in order to understand how a set stores values. To further understand a set we need to talk about something called Hashing.

# Hashing

Hashing uses a location value to store inputted data so it is easier for the set to find said values. Hashing makes it easier to check and retrieve values and uses 0(1) performance on top of that. This method of hashing uses modulus of the given value to store it in a set. This concept can be a little complicated to understand at first. I will do my best to explain it.

Great! Another term - modulus. Modulus is the % in python which just means deviding and taking the decimal.

Back to hashing! Great.. so Hashing is a way to store data easily by the set. Think of the set as boxes that are empty but can store values as we give the set values, as dipicted below. In this example, we give the set a random like 164 and using hasing and modulus it devides it by 10 (since there are 10 boxes) and uses the remainder to sort the number. If we think about it further, we can use this idea with more numbers. Lets take 163, if we do 163 % 10 it equals 16.3 and gets stored in index 3. We will be facing a problem in a minute.

![Set_Hashing](https://user-images.githubusercontent.com/108925950/229272140-c07ea8cd-6fa4-4b1c-8d32-2d5caea05fd4.jpg)

So with this we can see how the set, using hashing, would store data that we input. The problem we run into is when we get two numbers that have the same modulus. So what do we do? Well there are a couple ways we can go about this. First we could just override the modulus thing and move to the next avalible spot. If we give the set 174 that will also return a 4 but 164 is already in that spot so the set will put it in the next avalible spot which would be index 5.

If we only have 10 numbers we are woking with then it is an option and we wouldnt have to worry. However, what if we are working with 100s of values? We have a way to get around this and arguably it is a better way. So youre inputting data into a set and have multiple values that have the same modulus. How we can get around this is to make a list within the one index in the set. It is now possible to store 164 and 174. Great more complication! Does this effect performance? yes obviously a little bit but not by much. Hashing with built-in functions are great with handling performance.

# operations/ Performance

Just like queues, sets have a lot of use in programming. Sets depend upon size usually a set and its operations are O(1) performance. The common operations sets use are as follows.

## Add:

The add operation adds a value to the set. surprising huh! I bet you would have never guessed! This operation uses peak performance because it is only doing one thing and thats worrying about hashing.


#### Python:

```
my_set.add()
```

## Remove:

Bet you wont guess what this operation does! It removes a value from the set. Crazy! This also uses O(1) because it to just uses one hash and find where it placed the value in one "loop" if you will. Meaning it doesnt have to loop more than once.

#### Python:

```
my_set.remove()
```

## Size:

The size operator will return the size of the set or the amount of values within it. it is easy to do this using the len() fuction.

```
len = len(my_set)
```

Other nothable operations are union, intersecttion.

# Code example

I want to show a visual example of everything we just learned. So what do we know about a set. Two things, order doesnt matter and sets dont allow duplicates. To show you this lets take the alphabet for instance.

you can easily make a set with the alphabet. It is also easy to see how a set works with an alphabet.

![Set Code Example final](https://user-images.githubusercontent.com/108925950/229303704-1fd8dd22-fb56-471f-bfc1-4df9fdea4e3d.jpg)

The results of this code show how sets work.


![Set Code example final 2](https://user-images.githubusercontent.com/108925950/229303818-9bde370c-83b3-4bb5-80b0-f77ca3cbf2cd.jpg)


# Try it yourself!

Below is a problem I've made to help you get familiar with and learn about sets. Try it yourself! You can do it!
[Problem](https://github.com/Cartman3/Data_Structures_Tutorial/blob/main/Set_try_yourself_problem.py)


Here is a solutioh to the problem: [Solution](https://github.com/Cartman3/Data_Structures_Tutorial/blob/main/Set_try_yourself_solution.py)

