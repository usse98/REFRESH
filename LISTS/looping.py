#Looping through a list is helpful when you want to perform an action for each item in the list.
#You can use a for loop to iterate through each item in the list.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")

print("Thank you, everyone. That was a great magic show!")
print("\n")

#You can also use a for loop to perform an action for each item in a list of numbers.
for value in range(1,6):
    print(value)
print("\n")

#Exercise 
pizzas = ['salame_piccante', 'napoletana', 'quattro_stagioni', 'margherita']
for pizza in pizzas:
    print(f"I would like to order a {pizza} I think it's the best one you have.")
    print(f"No problem I will get your {pizza} right away.\n")

print("is that all?")


