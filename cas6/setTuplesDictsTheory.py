### Dictionaries

# Creation:
# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Adding Elements:
# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'

# Deleting Elements:
# Deleting a key-value pair
del my_dict['age']

# Using pop() to remove and return a value
email = my_dict.pop('email')

# Accessing Elements:
# Accessing a value by key
print(my_dict['name'])  # Output: Alice

# Using get() to avoid KeyError
age = my_dict.get('age', 'Not Found')


### Sets

# Creation:
# Creating a set
my_set = {1, 2, 3, 4}

# Creating an empty set
empty_set = set()

# Adding Elements:
# Adding an element
my_set.add(5)

# Deleting Elements:
# Removing an element
my_set.remove(3)  # Raises KeyError if 3 is not present

# Using discard() to avoid KeyError
my_set.discard(3)

# Removing and returning an arbitrary element
element = my_set.pop()

# Accessing Elements:
# Checking for membership
print(2 in my_set)  # Output: True


### Tuples

# Creation:
# Creating a tuple
my_tuple = (1, 'apple', 3.5)

# Creating a single element tuple
single_element_tuple = (1,)

# Accessing Elements:
# Accessing elements by index
print(my_tuple[1])  # Output: apple

# Slicing tuples
sub_tuple = my_tuple[:2]


### Examples

# Dictionary Example

# Creating a dictionary to store student grades
grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'C'}

# Adding a new student's grade
grades['David'] = 'B+'

# Updating a student's grade
grades['Alice'] = 'A+'

# Deleting a student's record
del grades['Charlie']

# Accessing a student's grade
print(grades['Bob'])  # Output: B

# Safely getting a grade (returns None if the key is not found)
print(grades.get('Eve'))  # Output: None


# Set Example

# Creating a set of prime numbers
primes = {2, 3, 5, 7, 11}

# Adding a new prime number
primes.add(13)

# Removing a prime number
primes.remove(7)

# Checking for membership
is_prime = 11 in primes  # Output: True

# Removing an arbitrary element
arbitrary_prime = primes.pop()


# Tuple Example

# Creating a tuple to store a point in 3D space
point = (4, 5, 9)

# Accessing coordinates
x, y, z = point
print(f"x: {x}, y: {y}, z: {z}")

# Tuples as keys in a dictionary
location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}
print(location_data[(40.7128, -74.0060)])  # Output: New York

