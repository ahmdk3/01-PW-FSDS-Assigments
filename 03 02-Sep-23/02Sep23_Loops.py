# Question 1
# Write a Python program to print the numbers from 1 to 10 using a `for` loop.
for i in range(1, 11):
    print(i)

# Question 2
# Create a program that calculates the sum of all numbers in a list using a `for` loop.
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)

# Question 3
# Write a program to print the characters of a string in reverse order using a `for` loop.
string = "Hello, World!"
for char in reversed(string):
    print(char)

# Question 4
# Develop a program that finds the factorial of a given number using a `for` loop.
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# Question 5
# Create a program to print the multiplication table of a given number using a `for` loop.
n = 5
for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")

# Question 6
# Write a program that counts the number of even and odd numbers in a list using a `for` loop.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

# Question 7
# Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop.
for i in range(1, 6):
    square = i ** 2
    print(f"{i} squared is {square}")

# Question 8
# Create a program to find the length of a string without using the `len()` function.
string = "Hello, World!"
count = 0
for char in string:
    count += 1
print(count)

# Question 9
# Write a program that calculates the average of a list of numbers using a `for` loop.
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(average)

# Question 10
# Develop a program that prints the first `n` Fibonacci numbers using a `for` loop.
n = 10
a, b = 0, 1
for _ in range(n):
    print(a)
    a, b = b, a + b

# Question 11
# Write a program to check if a given list contains any duplicates using a `for` loop.
def has_duplicates(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False

my_list = [1, 2, 3, 4, 2]
if has_duplicates(my_list):
    print("The list contains duplicates")
else:
    print("The list does not contain duplicates")

# Question 12
# Create a program that prints the prime numbers in a given range using a `for` loop.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = 10
end = 50
for number in range(start, end + 1):
    if is_prime(number):
        print(number)

# Question 13
# Develop a program that counts the number of vowels in a string using a `for` loop.
string = "Hello, World!"
vowels = "AEIOUaeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"The number of vowels in the string is: {count}")

# Question 14
# Write a program to find the maximum element in a 2D list using a nested `for` loop.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max_value = float('-inf')

for row in matrix:
    for element in row:
        if element > max_value:
            max_value = element

print(f"The maximum element in the 2D list is: {max_value}")

# Question 15
# Create a program that removes all occurrences of a specific element from a list using a `for` loop.
my_list = [1, 2, 3, 2, 4, 2, 5]
element_to_remove = 2

new_list = []
for item in my_list:
    if item != element_to_remove:
        new_list.append(item)

print(new_list)

# Question 16
# Develop a program that generates a multiplication table for numbers from 1 to 5 using a nested `for` loop.
for i in range(1, 6):
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")

# Question 17
# Write a program that converts a list of Fahrenheit temperatures to Celsius using a `for` loop.
fahrenheit_temperatures = [32, 68, 100, 212]
celsius_temperatures = []

for fahrenheit in fahrenheit_temperatures:
    celsius = (fahrenheit - 32) * 5/9
    celsius_temperatures.append(celsius)

print(celsius_temperatures)

# Question 18
# Create a program to print the common elements from two lists using a `for` loop.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)

print(common_elements)

# Question 19
# Develop a program that prints the pattern of right-angled triangles using a `for` loop. Use ‘*’ to draw the pattern
n = 5

for i in range(1, n + 1):
    print('* ' * i)

# Question 20
# Write a program to find the greatest common divisor (GCD) of two numbers using a `for` loop.
import math

a = 24
b = 36
a1=a
b1=b
while b1:
    a1, b1=b1, a1%b1
gcd = a1
print(f"The GCD of {a} and {b} is: {gcd}")


# Advanced Level:

# Question 21
# Create a program that calculates the sum of the digits of numbers in a list using a list comprehension.
numbers = [123, 45, 67, 89, 12]
sum_of_digits = [sum(int(digit) for digit in str(num)) for num in numbers]
print(sum_of_digits)

# Question 22
# Write a program to find the prime factors of a given number using a `for` loop and list comprehension.
def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors

number = 60
factors = prime_factors(number)
print(factors)

# Question 23
# Develop a program that extracts unique elements from a list and stores them in a new list using a list comprehension.
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = list(set(original_list))
print(unique_elements)

# Question 24
# Create a program that generates a list of all palindromic numbers up to a specified limit using a list comprehension.
limit = 100
palindromic_numbers = [num for num in range(1, limit + 1) if str(num) == str(num)[::-1]]
print(palindromic_numbers)

# Question 25
# Write a program to flatten a nested list using list comprehension.
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)

# Question 26
# Develop a program that computes the sum of even and odd numbers in a list separately using list comprehension.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even = sum(num for num in numbers if num % 2 == 0)
sum_of_odd = sum(num for num in numbers if num % 2 != 0)
print(f"Sum of even numbers: {sum_of_even}, Sum of odd numbers: {sum_of_odd}")

# Question 27
# Create a program that generates a list of squares of odd numbers between 1 and 10 using list comprehension.
squares_of_odd_numbers = [num**2 for num in range(1, 11) if num % 2 != 0]
print(squares_of_odd_numbers)

# Question 28
# Write a program that combines two lists into a dictionary using list comprehension.
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = {k: v for k, v in zip(keys, values)}
print(dictionary)

# Question 29
# Develop a program that extracts the vowels from a string and stores them in a list using list comprehension.
input_string = "Hello, World!"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_list = [char for char in input_string if char in vowels]
print(vowel_list)

# Question 30
# Create a program that removes all non-numeric characters from a list of strings using list comprehension.
input_list = ["abc123", "xyz456", "789def"]
numeric_characters = [char for string in input_list for char in string if char.isdigit()]
print(numeric_characters)

# Challenge Level:

# Question 31
# Write a program to generate a list of prime numbers using the Sieve of Eratosthenes algorithm and list comprehension.
def sieve_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for current in range(2, int(limit**0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, limit + 1, current):
                sieve[multiple] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

limit = 100
prime_numbers = sieve_eratosthenes(limit)
print(prime_numbers)

# Question 32
# Create a program that generates a list of all Pythagorean triplets up to a specified limit using list comprehension.
limit = 20
pythagorean_triplets = [(a, b, c) for a in range(1, limit + 1) for b in range(a, limit + 1) for c in range(b, limit + 1) if a**2 + b**2 == c**2]
print(pythagorean_triplets)

# Question 33
# Develop a program that generates a list of all possible combinations of two lists using list comprehension.
list1 = [1, 2, 3]
list2 = ['a', 'b']
combinations = [(x, y) for x in list1 for y in list2]
print(combinations)

# Question 34
# Write a program that calculates the mean, median, and mode of a list of numbers using list comprehension.
from statistics import mean, median, mode

numbers = [1, 2, 3, 4, 4, 5, 5, 5]
mean_value = mean(numbers)
median_value = median(numbers)
mode_value = mode(numbers)
print(f"Mean: {mean_value}, Median: {median_value}, Mode: {mode_value}")

# Question 35
# Create a program that generates Pascal's triangle up to a specified number of rows using list comprehension.
def generate_pascals_triangle(num_rows):
    triangle = [[1]]
    for i in range(1, num_rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

num_rows = 5
pascals_triangle = generate_pascals_triangle(num_rows)
print("Pascal's Triangle:")
for row in pascals_triangle:
    print(row)

# Question 36
# Develop a program that calculates the sum of the digits of a factorial of numbers from 1 to 5 using list comprehension.
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

factorial_sums = [sum_of_digits(math.factorial(n)) for n in range(1, 6)]
print(factorial_sums)

# Question 37
# Write a program that finds the longest word in a sentence using list comprehension.
sentence = "This is a sample sentence with the longest word"
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word in the sentence is: {longest_word}")

# Question 38
# Create a program that filters a list of strings to include only those with more than three vowels using list comprehension.
word_list = ["apple", "banana", "grape", "elephant", "ostrich", "aardvark"]
vowel_count_filter = [word for word in word_list if sum(1 for char in word if char.lower() in 'aeiou') > 3]
print(f"Words with more than 3 vowels: {vowel_count_filter}")

# Question 39
# Develop a program that calculates the sum of the digits of numbers from 1 to 1000 using list comprehension.
sum_of_digits_1000 = sum(sum(int(digit) for digit in str(num)) for num in range(1, 1001))
print(f"Sum of digits of numbers from 1 to 1000: {sum_of_digits_1000}")

# Question 40
# Write a program that generates a list of prime palindromic numbers using list comprehension.
def is_palindrome(num):
    return str(num) == str(num)[::-1]

prime_palindromic_numbers = [num for num in prime_numbers if is_palindrome(num)]
print(f"Prime palindromic numbers: {prime_palindromic_numbers}")