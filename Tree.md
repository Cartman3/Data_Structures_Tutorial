# Tree

## Introduction

We've now come to trees, yes I said tree's. I know youre thinking of a tree outside in your yard. You wouldn't be worng for thinking that because that is a great way to think about trees in programming. Trees in programming are like linked lists (I know we didnt go over linked lists in this tutorial). A quick explination, a linked list is a list that is linked with the value in front of it and behind it. Wild right! So the value right next to a specfic one knows whats happening to it. Its like holding hands. If youre holding hands with someone and that person starts walking away, well you'll know they're walking away because you are holding hands or "connected". In other words they have nodes that are connected to the front and back nodes or values.

Trees act the same except they can have multiple nodes that branch off to other nodes. In this way you can actually think of it like a tree. Trees start as one stump and as they grow they grow branches and those branches grow branches and so on. They all can be lead back to the same stump. This is excatly what a tree in programming is.


## How trees work

Maybe you need a better ecample. Lets use the computer! In the real world lets start by saying we have 5 classes in college; Math, Science, History, Art, and Religion. You have homework for that require you to save documents on your computer for each. It would get quite disorganized to just save all these documents on your desktop. So, logically we could make folders for each class and save each homework assignment there. Going further we could even make folders within those classes for the weeks of school. Just like the example below

![Trees_how_does_it_work](https://user-images.githubusercontent.com/108925950/229310381-b6583d49-6a0f-4f59-9f49-6f220a3b4968.jpg)

As you can see each "child" folder is within the "parant" folder. Another example that may be easier is below.

![Tree_example2](https://user-images.githubusercontent.com/108925950/229310566-3066c613-ab65-4502-81e5-5c52da7bc3f1.jpg)

As you can see it is a tree. We can make as many child nodes as you need to organize how you like. This may impact performace but we will talk about that later on. We now have to talk about binary trees.

## Binary Tree

The example above isnt entirely how trees in programming work but it is a good start. A binary tree acts a little different then the first example There are some important characteristics noted below.
<ul>
  <li>We are limited to only two child nodes branching off of a parent node.</li>
  <li>Leafs are ordered from right to left, lowest value to higest value.</li>
  <li>You can have parent, child, and sibling nodes. (as shown in the example below)</li>
  <li>Nodes under a parent are called sub-trees.</li>
</ul>

![Tree_example2](https://user-images.githubusercontent.com/108925950/229310566-3066c613-ab65-4502-81e5-5c52da7bc3f1.jpg)

#### inputting data into a tree

Now onto inserting data. Fornunatly, this is eay to understand! Knowing that a tree organizes data from left to right, lowest to higest. we can conclude what would happen if we were to insert certain data. Look at the example below.
  
 ![Tree_Binary](https://user-images.githubusercontent.com/108925950/229311907-f4da68c6-686f-4df1-9523-919753a5f7cc.jpg)

This method is comparing each value and then based on if it is less than or greater than the stored value it will sort it into the repective child class. Seems great right. Hold on to your hat because im going to throw you another problem! AHHHH!
 
What if we are inputting a 10, 12, 15, 20? They would all fall to the right and that would cause an unbalance in the tree. Yes, unbalanced tree rasises a problem.

#### Balanced trees

We run into a problem if our trees are unbalanced. This has everything to do with the height of the tree. An unbalaced tree vs a balanced tree may look like this:
The unbalanced tree is to the right and the balanced is to the left.

  ![Balancing trees](https://user-images.githubusercontent.com/108925950/229312229-879651cf-4039-4f86-8cce-2215e01323d6.jpg)
  
The tree starts to look unbalanced when the hight of the tree does not level out and stay fairly even. if not delt with the performance of the program or tree can drop significatly. The example obove shows how we can deal with this. The best way is to insert the middle number first, that way the tree will always be evenly distributed and maintain a relativly low hieght, as opposed to starting with the first number and (log n) the height.


## Operations/ Performance!

Trees have important operators that go along with them as well. Some of the most common one are follows:

### Insert:
The insert operator allows you to adds values to the tree. The tree then sorts it with O(log n) effeciency.

### Remove:
The remove operator removes nodes from the tree. Also O(log n) because it uses recursion.

### Height:
This operator searches through the tree and returns the height of the tree. Uses O(n)

### Contains
This operator searches through the tree and compares each vlaue. Uses O(log n)

## code example


# Try it yourself!

Below is a chanllenge for you! Become familiar with seting up a BST! You got this! [Try it yourself!](https://github.com/Cartman3/Data_Structures_Tutorial/blob/main/Trees_Problem.py)
![Trees_prob_pic](https://user-images.githubusercontent.com/108925950/229315364-4bc4e0ab-dcd7-4f8b-a209-a9ece2c9c54b.jpg)

Here is a possible solution: Solution

