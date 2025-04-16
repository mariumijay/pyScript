#Part 01

#print hellowrold 5 times
print("Print  5 times hello world")
count = 0
while count < 5:
    print("HelloWorld")

    count += 1

# 2. Print the first ten numbers (1-10)

print("Print first Ten numbers")
count = 1
while count <= 10:
    print(count)
    count += 1

# 3. Print the first 11 numbers in reverse order (10-0)
print("Print first eleven numbers in reverse order")
count = 10
while count >= 0:
    print(count)
    count -= 1

# 4. Print positive numbers (1-15)

print("Print positive numbers")
count = 1
while count <= 15:
    print(count)
    count += 1

# 5. Print negative numbers (-1 to -15)

print("Print negative numbers")
count = -1
while count >= -15:
    print(count)
    count -= 1

# 6. Factorial of a number (9)

print("Print Factorial numbers")
num = 9
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)

# 7. Check if a number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# 8. Generate a multiplication table of 12
num = 12
count = 1
while count <= 10:
    print(f"{num} x {count} = {num * count}")
    count += 1

# 9. Print the sum of the first 10 natural numbers
count = 1
sum_natural_numbers = 0
while count <= 10:
    sum_natural_numbers += count
    count += 1
print(f"The sum of the first 10 natural numbers is: {sum_natural_numbers}")

# 10. Print right-angled triangle using stars (*)
count = 1
while count <= 5:
    print('*' * count)
    count += 1

#part 02

# 1. Print HelloWorld five times
for _ in range(5):
    print("HelloWorld")

# 2. Print the first ten numbers (1-10)
for num in range(1, 11):
    print(num)

# 3. Print the first 11 numbers in reverse order (10-0)
for num in range(10, -1, -1):
    print(num)

# 4. Print positive numbers (1-15)
for num in range(1, 16):
    print(num)

# 5. Print negative numbers (-1 to -15)
for num in range(-1, -16, -1):
    print(num)

# 6. Print even and odd numbers between 1 and 100
print("Even numbers:")
for num in range(2, 101, 2):
    print(num)

print("Odd numbers:")
for num in range(1, 101, 2):
    print(num)

# 7. Print all alphabets (A-Z)
for char in range(65, 91):  # A to Z
    print(chr(char), end=' ')
print()

# For lowercase (a-z)
for char in range(97, 123):  # a to z
    print(chr(char), end=' ')
print()

# 8. Factorial of a number (9)
factorial = 1
for num in range(1, 10):
    factorial *= num
print(factorial)

# 9. Check if a number is a palindrome
num = input("Enter a number: ")
if num == num[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

# 10. Print right-angled triangle using stars (*)
for i in range(1, 6):
    print('*' * i)

# 11. Count vowels and consonants in a string
string = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

# 12. Generate a multiplication table of 12
for i in range(1, 11):
    print(f"12 x {i} = {12 * i}")

# 13. Print squares of numbers from 1 to 10
print("Squares of numbers from 1 to 10:")
for num in range(1, 11):
    print(f"{num}^2 = {num**2}")

# 13. Print cubes of numbers from 1 to 10
print("Cubes of numbers from 1 to 10:")
for num in range(1, 11):
    print(f"{num}^3 = {num**3}")

#Part 03

# 1. Create a list of even numbers between 1 to 10
even_numbers = []
for num in range(1, 11):
    if num % 2 == 0:
        even_numbers.append(num)
print("Even numbers between 1 to 10:", even_numbers)

# 2. Print Pyramid triangle using stars (*)
rows = 5  # Height of the pyramid
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")  # Print spaces for alignment
    for k in range(2 * i - 1):
        print("*", end="")  # Print stars
    print()  # Newline for the next row


# 3. Printing first 20 prime numbers
prime_numbers = []
num = 2
while len(prime_numbers) < 20:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
    num += 1
print("First 20 prime numbers:", prime_numbers)

#Part 04
# 1. Find the first even number in a list using a break statement
numbers = [1, 3, 5, 8, 10, 13, 15]
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        print(f"The first even number is: {num}")
        break  # Exit the loop after finding the first even number

# 2. Print only odd numbers from a list using continue and skip the iteration if the current number is 7
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num == 7:
        continue  # Skip this iteration if the number is 7
    if num % 2 != 0:  # Check if the number is odd
        print(num)

# 3. Print 1-20 even numbers from a list using continue and skip the iteration if the current number is 5
for num in range(1, 21):
    if num == 5:
        continue  # Skip the iteration if the current number is 5
    if num % 2 == 0:  # Check if the number is even
        print(num)

# 4. Create a list of odd numbers from 1 to 20 using a break statement
odd_numbers = []
for num in range(1, 21):
    if num % 2 != 0:  # Check if the number is odd
        odd_numbers.append(num)
    if len(odd_numbers) == 10:  # Stop after finding the first 10 odd numbers
        break
print("List of first 10 odd numbers:", odd_numbers)

#Part 05

# 1. Print a Welcome Message
def welcome_message():
    print("Welcome to the Python Programming World!")

# Calling the function
welcome_message()

# 2. Add Two Numbers
def add_numbers(a, b):
    return a + b

# Calling the function
result = add_numbers(5, 3)
print(f"The sum is: {result}")

# 3. Check Even or Odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Calling the function
print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd

# 4. Find the Factorial of a Number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
print(factorial(5))  # Output: 120

# 5. Calculate the Area of a Circle
import math

def area_of_circle(radius=5):
    return math.pi * (radius ** 2)

# Calling the function
print(area_of_circle())      # With default value
print(area_of_circle(10))    # With custom value

# 6. Check if a Number is Prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Calling the function
print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False

# 7. Find the Maximum of Three Numbers
def find_max(a, b, c):
    return max(a, b, c)

# Calling the function
print(find_max(3, 7, 2))  # Output: 7

# 8. Calculate Simple Interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Calling the function
print(simple_interest(1000, 5, 2))  # Output: 100.0

# 9. Generate Fibonacci Sequence
def fibonacci():
    fib_sequence = [0, 1]
    while len(fib_sequence) < 10:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Calling the function
print(fibonacci())

# 10. Reverse a String
def reverse_string(s):
    return s[::-1]

# Calling the function
print(reverse_string("hello"))  # Output: "olleh"

# 11. Check for Palindrome
def is_palindrome(value):
    return str(value) == str(value)[::-1]

# Calling the function
print(is_palindrome(121))  # Output: True
print(is_palindrome("racecar"))  # Output: True

# 12. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

# Calling the function
print(count_vowels("hello"))  # Output: 2

# 13. Find the Length of a List Without Using len()
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# Calling the function
print(list_length([1, 2, 3, 4, 5]))  # Output: 5

# 14. Sum of Digits of a Number
def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits += n % 10
        n //= 10
    return sum_digits

# Calling the function
print(sum_of_digits(123))  # Output: 6

# 15. Sort a List Using a Function
def sort_list(lst):
    return sorted(lst)

# Calling the function
print(sort_list([5, 2, 8, 1, 3]))  # Output: [1, 2, 3, 5, 8]

# 16. Print a String multiple times
def print_multiple_times(s, times=3):
    for _ in range(times):
        print(s)

# Calling the function
print_multiple_times("Hello")  # Output: Prints "Hello" 3 times
print_multiple_times("Hi", 2)  # Output: Prints "Hi" 2 times



#Part 07
# 1. Find the Length of a String
def string_length(s):
    return len(s)

# Calling the function
print(string_length("Hello World"))  # Output: 11

# 2. Copy One String to Another
def copy_string(s):
    copied_string = s
    return copied_string

# Calling the function
original_string = "Python"
copied_string = copy_string(original_string)
print(copied_string)  # Output: Python

# 3. Concatenate Two Strings
def concatenate_strings(s1, s2):
    return s1 + s2

# Calling the function
str1 = "Hello "
str2 = "World!"
print(concatenate_strings(str1, str2))  # Output: Hello World!

# 4. Compare Two Strings
def compare_strings(s1, s2):
    if s1 == s2:
        return "Strings are equal."
    else:
        return "Strings are not equal."

# Calling the function
print(compare_strings("Python", "Python"))  # Output: Strings are equal.
print(compare_strings("Python", "Java"))    # Output: Strings are not equal.

# 5. Convert a String to Uppercase and Lowercase
def convert_case(s):
    return s.upper(), s.lower()

# Calling the function
original_string = "I am Python Programmer"
upper_case, lower_case = convert_case(original_string)
print(f"Uppercase: {upper_case}")  # Output: I AM PYTHON PROGRAMMER
print(f"Lowercase: {lower_case}")  # Output: i am python programmer

# 6. Reverse a String
def reverse_string(s):
    return s[::-1]

# Calling the function
print(reverse_string("PROGRMMER"))  # Output: REMMARGOP

# 7. Count Words in a String
def count_words(s):
    return len(s.split())

# Calling the function
print(count_words("I am Python Programmer"))  # Output: 4

# 8. Find Duplicate Characters in a String
def find_duplicates(s):
    seen = set()
    duplicates = set()
    for char in s:
        if char in seen:
            duplicates.add(char)
        else:
            seen.add(char)
    return duplicates

# Calling the function
print(find_duplicates("ALIZA"))  # Output: {'A'}

#Part 08

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('AILab')
    elif num % 3 == 0:
        print('AI')
    elif num % 5 == 0:
        print('Lab')
    else:
        print(num)

#Part 09

def analyze_text(text):
    counts = {'uppercase': 0, 'lowercase': 0, 'digits': 0}
    
    for char in text:
        if char.isupper():
            counts['uppercase'] += 1
        elif char.islower():
            counts['lowercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
    
    return counts

# Example usage:
text = "Hello World 123"
result = analyze_text(text)
print(result)


#Part 10

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage:
sentence = "Artificial Intelligence Lab"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)

