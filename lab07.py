
#tuple
emptyTuple=()
print(emptyTuple)

# Tuple with multiple elements
my_tuple = (1, 2, 3, "hello", 4.5)

# Single element tuple (comma zaroori hai)
single_element_tuple = (5,)  


# print digit
t = (10, 20, 30, 40, 50)
print(t[0])  # Output: 10
print(t[2])  # Output: 30


# print last digit

print(t[-1])

#02 

#ADD Item
# Original tuple
my_tuple = (1, 2, 3)

# Tuple ko list mein convert karna
temp_list = list(my_tuple)

# List mein naya item add karna
temp_list.append(4)

# Wapas tuple mein convert karna
my_tuple = tuple(temp_list)

print(my_tuple)  # Output: (1, 2, 3, 4)




#03
t = ("apple", "Mango", "Banana")  # Original tuple
y = list(t)  # Convert tuple to list
y.remove("Banana")  # Remove item
t = tuple(y)  # Convert back to tuple
print(t)  # Output: ('apple', 'Mango')

#04
#range slicing

t = (10, 20, 30, 40, 50, 60, 70)

# Index 1 se 4 tak (4 included nahi hoga)
print(t[1:4])  # Output: (20, 30, 40)

# Start se index 3 tak
print(t[:3])   # Output: (10, 20, 30)

# Index 2 se end tak
print(t[2:])   # Output: (30, 40, 50, 60, 70)

# Last ke 3 elements
print(t[-3:])  # Output: (50, 60, 70)

# Step size ka use (har dusra element)
print(t[::2])  # Output: (10, 30, 50, 70)


#DICTIONERY

#syntax
my_dict = {
    "name": "Marium",
    "age": 21,
    "city": "Lahore"
}

print(my_dict["name"])  # Output: Marium

my_dict["age"] = 22  # Update value
my_dict["country"] = "Pakistan"  # Add new key-value pair
my_dict.pop("city")  # Remove key
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.items())  # Get all key-value pairs

#Nested Dictionery  (ik dic ky andr dusri dic rkhwai ha)

students = {
    "student1": {"name": "Marium", "age": 21, "city": "Lahore"},
    "student2": {"name": "Ayesha", "age": 22, "city": "Karachi"}
}

print(" Print Nested Dic : " , students)
print(" Print  Dic item : " ,students["student1"]["name"])  # Output: Marium
print(" Print  Dic item: " ,students["student2"]["city"])  # Output: Karachi
print(" Print Nested Dic : " , students["student1"])

#set syntax
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# DUPLICATE Values not Allowed
s = {1, 2, 2, 3, 4}
print(s)  # Output: {1, 2, 3, 4}

#ADD sinlge Item
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}

#ADD Multiple 
s.update([5, 6, 7])  # List add ki
print("01." , s)  # Output: {1, 2, 3, 4, 5, 6, 7}

s.update((8, 9))  # Tuple add kiya
print("02." ,s)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

#add one set into another set
A = {1, 2, 3}
B = {4, 5, 6}

A.update(B)
print(A)  # Output: {1, 2, 3, 4, 5, 6}

#Remove Item

s = {1, 2, 3, 4, 5}
s.remove(3)  
print(s)  # Output: {1, 2, 4, 5}

#s.remove(10)  #  Error dega (KeyError)

#discard() (Error nahi dega agar item na mile)

s.discard(4)
print(s)  # Output: {1, 2, 5}

s.discard(10)  #  No error

#pop() (Random element remove karega)

removed_item = s.pop()
print(s)  
print("Removed:", removed_item)

#clear() (Pura set empty karna)

s.clear()
print(s)  # Output: set()

#Union Sets
A = {1, 2, 3}
B = {3, 4, 5}

C = A.union(B)
print(C)  # Output: {1, 2, 3, 4, 5}

#Update
A.update(B)
print(A)  # Output: {1, 2, 3, 4, 5} (A update ho gaya)

#Intersection
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A & B  # Using `&`
print(C)  # Output: {3, 4}

D = A.intersection(B)  # Using `intersection()`
print(D)  # Output: {3, 4}

#Difference
C = A - B  # A me jo B me nahi
print(C)  # Output: {1, 2}

D = B - A  # B me jo A me nahi
print(D)  # Output: {5, 6}

E = A.difference(B)  # Using `difference()`
print(E)  # Output: {1, 2}


#IF-Else Statment

#Check Number is Positive
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number.")
else:
    print("Not a positive number.")

# Check Number is Greater
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater.")
elif b > a:
    print(f"{b} is greater.")
else:
    print("Both are equal.")

#elif Statment   (if - elif -else)

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number.")
else:
    print("Zero.")


