classe = ["John", "Mary", "Bob", "Alice", "Tom"]
print(classe[0])  # John
print(classe[3])  # Alice
print(classe[-1]) # Tom
# Using -1 to access the last element
greetings = f"Hello, my name is {classe[3]}, from today I will be your classmate!"
print(greetings)

# Changing, Adding, and Removing Elements
classe[2] = "Robert"  # Change Bob to Robert
print(classe)   # ['John', 'Mary', 'Robert', 'Alice', 'Tom']
classe.append("Emma")  # Add Emma to the end
print(classe)   # ['John', 'Mary', 'Robert', 'Alice', 'Tom', 'Emma']
classe.insert(1, "Michael")  # Insert Michael at index 1
print(classe)   # ['John', 'Michael', 'Mary', 'Robert', 'Alice', 'Tom', 'Emma']
classe.remove("Alice")  # Remove Alice
print(classe)   # ['John', 'Michael', 'Mary', 'Robert', 'Tom', 'Emma']
removed_student = classe.pop()  # Remove and return the last element
print(removed_student)  # Emma
print(classe)   # ['John', 'Michael', 'Mary', 'Robert', 'Tom']
del classe[0]  # Delete the first element
print(classe)   # ['Michael', 'Mary', 'Robert', 'Tom']
classe.clear()  # Clear the list
print(classe)   # []

# Organizing a List
classe = ["John", "Mary", "Bob", "Alice", "Tom"]
classe.sort()  # Sort the list alphabetically
print(classe)   # ['Alice', 'Bob', 'John', 'Mary', 'Tom']
classe.sort(reverse=True)  # Sort the list in reverse alphabetical order
print(classe)   # ['Tom', 'Mary', 'John', 'Bob', 'Alice']
print(sorted(classe))  # Print a sorted version of the list without changing the original
print(classe)   # Original list remains unchanged
classe.reverse()  # Reverse the order of the list
print(classe)   # ['Tom', 'Mary', 'John', 'Bob', 'Alice']
print(len(classe))  # Print the number of elements in the list