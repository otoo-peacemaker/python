# Example of a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
print(my_list[0])  # Accessing the first element (Output: 1)
print(my_list[-1])  # Accessing the last element (Output: 5)

print(my_list[1:3])  # Slicing from index 1 to 2 (Output: [2, 3])
print(my_list[:3])   # Slicing from the beginning to index 2 (Output: [1, 2, 3])
print(my_list[2:])   # Slicing from index 2 to the end (Output: [3, 4, 5])

my_list[0] = 0  # Modifying the first element
print(my_list)  # Output: [0, 2, 3, 4, 5]

my_list.remove(2)  # Removing a specific element
print(my_list)    # Output: [0, 3, 4, 5]
popped_element = my_list.pop()  # Removing and returning the last element
print(popped_element)  # Output: 5
append_list = my_list.append(9)  # updating last element with 9
print(my_list)  # Output: [0, 3, 4, 9]

# Creating a new list using list comprehension
new_list = [x * 2 for x in my_list]  # multiply each value in the list by two
print(new_list)  # Output: [0, 6, 8, 10, 18]


# Example of a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing the first element (Output: 1)
print(my_tuple[-1])  # Accessing the last element (Output: 5)

print(my_tuple[1:3])  # Slicing from index 1 to 2 (Output: (2, 3))
print(my_tuple[:3])   # Slicing from the beginning to index 2 (Output: (1, 2, 3))
print(my_tuple[2:])   # Slicing from index 2 to the end (Output: (3, 4, 5))

another_tuple = (6, 7, 8)  # Concatenating tuples:
concatenated_tuple = my_tuple + another_tuple
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

a, b, c, d, e = my_tuple  # unpacking tuples
print(a, b, c, d, e)  # Output: 1 2 3 4 5

print(my_tuple.count(2))  # Count occurrences of element 2 (Output: 1)
print(my_tuple.index(3))  # Find index of element 3 (Output: 2)


# Example of a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# Accessing value using key
print(my_dict['name'])  # Output: John
# Accessing value using get() method
print(my_dict.get('age'))  # Output: 30

# Adding a new key-value pair
my_dict['job'] = 'Engineer'
# Updating the value of an existing key
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair using del
del my_dict['city']
# Removing a key-value pair using pop() method
my_dict.pop('job')
print(my_dict)  # Output: {'name': 'John', 'age': 31}

# Checking if a key exists:
print('name' in my_dict)  # Output: True
print('job' in my_dict)   # Output: False


# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(key, value)

# Clearing the dictionary:
my_dict.clear()
print(my_dict)  # Output: {}


# These examples demonstrate the usage of list, tuple, and dictionary data types in Python.
# Lists are mutable sequences, meaning the values can be changed or modified
# tuples are immutable sequences, and
# dictionaries are unordered collections of key-value pairs

