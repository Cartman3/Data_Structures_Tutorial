primary_colors = set()
nonpri_colors = set()

print(primary_colors)
print(nonpri_colors)

def intersection_of_sets(primary_colors, nonpri_colors):
    result = []
    for i in primary_colors:
        if i in nonpri_colors:
            result.append(i)
    return result

###################
    # Problem 1 #
###################

# You can mess with this to get familiar with add and remove functions
# Add colors to primary color set and non primary color set.
# The add function also takes in strings you'll need to make multiple statements or use ,

print()
print("----------Problem 1----------")
print()

primary_colors.add('Red')
primary_colors.add('Yellow')
primary_colors.add('Yellow')
primary_colors.add('Blue')

nonpri_colors.add('Orange')
nonpri_colors.add('Green')
nonpri_colors.add('Violet')
nonpri_colors.add('Orange')

print(primary_colors) # prints the colors in the set
print(nonpri_colors)  # prints the colors in the set
pass

# Try using duplicates!
# Using the len() you can see how many are in each set
# You can also try removing the elements


###################
    # Problem 2 #
###################

# This problem will be working with the intersection fuction
###### Make sure to add the same color to each set like white to both sets #####

print()
print('----------Problem 2----------')
print()

primary_colors.add('Red')
primary_colors.add('Yellow')
primary_colors.add('Blue')
primary_colors.add('White')
primary_colors.add('Black')

nonpri_colors.add('Green')
nonpri_colors.add('Violet')
nonpri_colors.add('Orange')
nonpri_colors.add('White')
nonpri_colors.add('Black')

print(primary_colors) # prints the colors in the set
print(nonpri_colors)  # prints the colors in the set

print(intersection_of_sets(primary_colors, nonpri_colors)) # 'White'