# lists are usufull if you want to change the values.
# tuples are usufull if you want to make sure the values stay the same. Immutable.
# A tuple is identical to a list, but you use parentheses instead of square brackets.
dimension = ( 200, 50)
print(dimension[0])
print(dimension[1])
dimension[0] = 250
# dimension[0] = 250 # This will give an error because tuples are immutable.


