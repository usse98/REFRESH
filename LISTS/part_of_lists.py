# Slicing a List, working with specific parts of a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# Looping through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # This creates a copy of the list

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)