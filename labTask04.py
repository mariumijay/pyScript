#Tuple items ko positive aur negative indexes se access karna
t = ("apple", "banana", "cherry", "date", "fig")

#`Positive Indexing (0 se start hota hai)
print("Positive Indexing")
print(t[0])  # Output: apple
print(t[2])  # Output: cherry
print(t[4])  # Output: fig

print("Negative Indexing")
#Negative Indexing (-1 se start hota hai, last se count hota hai)**
print(t[-1])  # Output: fig
print(t[-3])  # Output: cherry
print(t[-5])  # Output: apple

#02
t = ("apple", "banana", "cherry", "date", "fig", "grape", "kiwi")

# ✅ **Positive Indexing (left to right)**
print("Positive Indexing (left to right)")
print(t[1:4])   # Output: ('banana', 'cherry', 'date')
print(t[:3])    # Output: ('apple', 'banana', 'cherry')
print(t[2:])    # Output: ('cherry', 'date', 'fig', 'grape', 'kiwi')

print("Negative Indexing (right to left)")
# ✅ **Negative Indexing (right to left)**
print(t[-4:-1])  # Output: ('date', 'fig', 'grape')
print(t[-3:])    # Output: ('fig', 'grape', 'kiwi')
print(t[:-2])    # Output: ('apple', 'banana', 'cherry', 'date', 'fig')

print("Mixing Positive & Negative Indexes")
# ✅ **Mixing Positive & Negative Indexes**
print(t[1:-2])   # Output: ('banana', 'cherry', 'date', 'fig')

#03
# Empty list
my_list = []

#  Append() - Single item add karna
my_list.append(10)

#  Extend() - Multiple items ek saath add karna
my_list.extend([20, 30, 40])

#  Insert() - Specific index pe item insert karna
my_list.insert(2, 25)  # Index 2 pe 25 insert hoga

# + Operator - List ko dusri list sath concatenate karna
my_list += [50, 60]

print(my_list)  

#04
# Original tuple
t = ("apple", "banana", "cherry")
print(t)

# Convert to list
temp_list = list(t)

# Change item at index 1
temp_list[1] = "blueberry"

# Convert back to tuple
t = tuple(temp_list)

print(t)  

#05
# Original tuple
fruits = ("apple", "banana", "cherry")

# Adding a new tuple using concatenation
new_fruits = fruits + ("mango", "orange")
print("Concatenated Tuple:", new_fruits)

# Adding a new tuple as a nested tuple
nested_fruits = (fruits, ("mango", "orange"))
print("Nested Tuple:", nested_fruits)

# Adding a single tuple dynamically
extra_fruits = ("grape",)
final_fruits = new_fruits + extra_fruits
print("Final Updated Tuple:", final_fruits)

#06
# Creating a tuple
fruit = ("apple", "banana", "cherry")
print( "origional typle of fruits: ",fruit)
# Deleting the entire tuple
del fruits
print("print after del : ", fruit)
# Trying to print will raise an error since the tuple no longer exists
# print(fruits)  # NameError: name 'fruits' is not defined
fruits = ("apple", "banana", "cherry")
print("another tuple of fruit:",fruits)
# Convert to list, remove item, and convert back to tuple
temp_list = list(fruits)
temp_list.remove("banana")  # Removes "banana"
fruits = tuple(temp_list)

print("after using remove() func:",fruits)  # Output: ('apple', 'cherry')

#07
#clear tuple
t = (10, 20, 30)
t = ()  # Assigning an empty tuple
print(t)  # Output: ()

t = (10, 20, 30)
del t  # Deletes the tuple

# print(t)  # This will give a NameError because t no longer exists

#08
#Join tuple using plu + and  sterick * 

t1=(10, 12,14)
t2 = (11, 13 , 15)

result1 = t1 + t2  # Concatenate
result2 = t1 * 5  #Repetation ( * repets the elements in the tuple)
print("Result of Joining Two Tuples using plus sign : ", result1)

result2 = t1 * 5  #Repetation ( * repets the elements in the tuple)
print("Result of Using * :", result2)

#09
# index of ‘Genetic Algorithms’ in the ai_concepts tuple.
ai_concepts=("ML","NN","GA","NLP","CV","DIP")
index = ai_concepts.index("GA")
print("Index of the Genetic Algorithms : " ,index)

#10
#access first and last element of the tuple

print("first element of the tuple : ", ai_concepts[0])
print("last element of the tuple : ", ai_concepts[-1])
print("slicing the element to print 1-3 :", ai_concepts[1:3])

#modification in tuple
modify=list(ai_concepts)
modify[0]= "machine Learning"
ai_concepts = tuple(modify)
print("print tuple after modification : ",ai_concepts)

#find the length using len()
length = len(ai_concepts)
print("print length of the tuple : ", length)

# D I C T I O N E R Y  T A S K
print( "D I C T I O N E R Y  T A S K ")

#01
#empty dictionery
dictionary= {}
print("eptyy dict :" ,dictionary)

#02
#Creating a dictionary with dict() function
emptyDic = dict()
print("eptyy dict :",emptyDic)

#03
#Creating a Dictionary with each item as a Pair.
dict={
    "Name":"Marium Ijaz",
    "Age" : 21,
    "City" : "Lahore"
}
print("Print Dict :",dict)

#04
#Python program to print Empty nested dictionary.

nestedDict ={
    "dict1" : {
        "name": "Marium", "Age": 21 ,"City" : "Lahore"
    },
    "dict2" : {
        "name": "Rayyan", "Age": 22 ,"City" : "Lahore"
    }
}
print("print nested dict :" ,nestedDict)
print("print first dic in nested dict :" ,nestedDict["dict1"])
print("print name in sec dic in nested dict :" ,nestedDict["dict2"]["name"])

#05
"""
Create a dictionary named ai_tools with keys as the AI concepts from the
ai_concepts tuple and values as examples of tools or libraries used in each
concept (e.g., ‘Machine Learning’: ‘scikit-learn’).
"""

ai_tools = {
    "Machine Learning": "scikit-learn",
    "Neural Networks": "TensorFlow",
    "Genetic Algorithms": "DEAP",
    "Natural Language Processing": "NLTK"
}

# changing in dict
ai_tools["Neural Networks"] ="Keras"
print("print dictionery after modification :" ,ai_tools)

# add new in dictionery
ai_tools["Neural Network"] ="Keras"
print("print dictionery after modification :" ,ai_tools)

# Arithmetic Operations

num1 = 10
num2 = 30
print("Addition : ",num1 + num2)
print("Subtraction : ",num1 - num2)
print("Multiplication : ",num1 * num2)
print("Division : ",num1 / num2)
print("Modulus : ",num1 % num2)
print("Exponential : ",num1 ** num2)

# student Record
#manually
studInfo = {
    "stud01" :{
    "name" : "Haseeb Iftikhar",
    "Age" : 20,
    "Marks" : 300},
     "stud02" :{
    "name" : "Sadoon Saeed",
    "Age" : 21,
    "Marks" : 250},
     "stud03" :{
    "name" : "Arwa Saleem",
    "Age" : 22,
    "Marks" : 350}
}
print("Student Informaton : ",studInfo)

students =[]
#user input
studInfo ={
    "name" : input("Enter Name:"),
    "age" : int(input("Enter  age :")),
    "marks" : float(input("Ente marks :"))
}
print("\nStudent Information:")
print(f"Name: {studInfo['name']}")
print(f"Age: {studInfo['age']}")
print(f"Marks: {studInfo['marks']}")

#allow user to add a new Student
students.append(studInfo)

print("\nStudent Information:")
print(f"Name: {studInfo['name']}")
print(f"Age: {studInfo['age']}")
print(f"Marks: {studInfo['marks']}")

add_more = input("\nDo you want to add another student? (yes/no): ")

# If the user wants to add more students
if add_more == 'yes':
    studInfo = {
        "name": input("Enter Name: "),
        "age": int(input("Enter age: ")),
        "marks": float(input("Enter marks: "))
    }
    students.append(studInfo)
    print("\nStudent Information:")
    print(f"Name: {studInfo['name']}")
    print(f"Age: {studInfo['age']}")
    print(f"Marks: {studInfo['marks']}")

    # Print all student details
print("\nAll Student Details:")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

# S E T S  T A S K
print("\nS E T S  T A S K")

# Add items in set
my_set = set()
my_set.add("AI")
my_set.add("ML")
print("After adding items:", my_set)

# Add Any Iterable
my_set.update(["DL", "NLP", "CV"])
print("After adding iterable:", my_set)

# Add and join two sets
set1 = {"AI", "ML"}
set2 = {"DL", "NLP"}
joined_set = set1.union(set2)
print("Joined Set:", joined_set)

# Remove items
my_set.remove("CV")
print("After remove():", my_set)
my_set.discard("DL")
print("After discard():", my_set)
my_set.pop()
print("After pop():", my_set)
my_set.clear()
print("After clear():", my_set)

# del will delete the set completely
sample_set = {1, 2, 3}
del sample_set

# Join two sets using union and update method
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b))
a.update(b)
print("After update():", a)

# Intersection & Difference
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}
print("Intersection:", x.intersection(y))
print("Difference:", x.difference(y))

# Completed and Upcoming Courses
completed_courses = {"ML", "NLP", "CV"}
upcoming_courses = {"DIP", "RL", "CV"}
unique_courses = completed_courses - upcoming_courses
print("Unique Completed Courses:", unique_courses)

# Integers sets program
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

set_a.add(7)
print("After adding 7 to set_a:", set_a)
set_b.remove(5)
print("After removing 5 from set_b:", set_b)
print("Is set_b subset of set_a?", set_b.issubset(set_a))


# C O N D I T I O N A L S  T A S K
print("\nC O N D I T I O N A L S  T A S K")

num = int(input("Enter a number: "))

# Positive number
if num > 0:
    print("Number is Positive")

# Negative number
if num < 0:
    print("Number is Negative")

# Greater than comparison
a = 10
b = 5
if a > b:
    print("a is greater than b")

# Lesser than comparison
if b < a:
    print("b is lesser than a")

# Greater and Lesser using if-else
if a > b:
    print("a is greater")
else:
    print("b is greater")

# Positive or Negative using if-else
if num >= 0:
    print("Positive number")
else:
    print("Negative number")

# Grade Classification
grade = int(input("Enter student's grade: "))
if grade > 90:
    print("Excellent")
elif 80 < grade <= 90:
    print("Good")
elif 70 < grade <= 80:
    print("Average")
else:
    print("Needs Improvement")

# AI Concept Suggestion
interest = input("Enter your area of interest (data/image/text): ").lower()
if interest == "data":
    print("Study Machine Learning")
elif interest == "image":
    print("Study Computer Vision")
elif interest == "text":
    print("Study Natural Language Processing")
else:
    print("Explore more AI fields!")
