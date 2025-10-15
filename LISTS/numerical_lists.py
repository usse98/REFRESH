# Numerical Lists, using the range() function.
numbers = list(range(1, 6))
print(numbers)

#You can also pass range() with only one argument, and it will start at 0 by default:
numbers = list(range(6))
print(numbers)

# if you want to make a range into a list you can convert the range using list()
numbers = list(range(7))
print(numbers)

# We can use range to make a list of the first 20 even numbers:
even_numbers = list(range(0, 41, 2))
print(even_numbers, "\n"*2)

# this tells python to start at 0, stop before 41, and count by 2s

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares, "\n"*2)
# This tells Python to start at 1 and stop before 11, and the loop adds the square of each value.

# Simple statistics with a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(min(digits))
print(max(digits))
print(sum(digits), "\n"*2)

# List Comprehensions, a way to generate a list in a single line of code.
squares = [value ** 3 for value in range(10)]
print(f"this is the cubic of numbers between 0 and 10: {squares}", "\n"*2)
# This is equivalent to the longer version above that used a for loop and append().

