# Task 1
print("Task 1:")
for i in range(1, 11):
    print(f"Task 1 - Number: {i}")

# Task 2
print("\nTask 2:")
print("Task 2 - The main difference between a for loop and a while loop in Python is that a for loop is used for iterating a specific number of times, while a while loop continues iterating as long as a condition is True.")

# Task 3
print("\nTask 3:")
sum_1_to_100 = 0
for i in range(1, 101):
    sum_1_to_100 += i
print(f"Task 3 - Sum of numbers from 1 to 100: {sum_1_to_100}")

# Task 4
print("\nTask 4:")
my_list = [1, 2, 3, 4, 5]
print("Task 4 - Iterating through a list using a for loop:")
for item in my_list:
    print(f"Item: {item}")

# Task 5
print("\nTask 5:")
my_list = [1, 2, 3, 4, 5]
product = 1
for item in my_list:
    product *= item
print(f"Task 5 - Product of elements in the list: {product}")

# Task 6
print("\nTask 6:")
print("Task 6 - Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(f"Even Number: {i}")

# Task 7
print("\nTask 7:")
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Task 7 - Factorial of {num} is: {factorial}")

# Task 8
print("\nTask 8:")
my_string = "Hello, World!"
print("Task 8 - Iterating through characters of the string:")
for char in my_string:
    print(f"Character: {char}")

# Task 9
print("\nTask 9:")
my_list = [4, 7, 1, 9, 3, 12, 8]
largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
print(f"Task 9 - Largest number in the list: {largest}")

# Task 10
print("\nTask 10:")
limit = 10
a, b = 0, 1
fibonacci_sequence = []
for i in range(limit):
    fibonacci_sequence.append(a)
    a, b = b, a + b
print(f"Task 10 - Fibonacci sequence up to limit: {fibonacci_sequence}")

# Task 11
print("\nTask 11:")
my_string = "Hello, World!"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in my_string:
    if char in vowels:
        vowel_count += 1
print(f"Task 11 - Number of vowels in the string: {vowel_count}")

# Task 12
print("\nTask 12:")
num = 5
print(f"Task 12 - Multiplication table for {num}:")
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")

# Task 13
print("\nTask 13:")
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print(f"Task 13 - Reversed List: {reversed_list}")

# Task 14
print("\nTask 14:")
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)
print(f"Task 14 - Common Elements: {common_elements}")

# Task 15
print("\nTask 15:")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Task 15 - Iterating through keys and values of a dictionary:")
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Task 16
print("\nTask 16:")
import math
num1 = 36
num2 = 48
gcd = math.gcd(num1, num2)
print(f"Task 16 - GCD of {num1} and {num2} is: {gcd}")

# Task 17
print("\nTask 17:")
my_string = "racecar"
is_palindrome = True
for i in range(len(my_string) // 2):
    if my_string[i] != my_string[-(i + 1)]:
        is_palindrome = False
        break
if is_palindrome:
    print("Task 17 - Palindrome")
else:
    print("Task 17 - Not a palindrome")

# Task 18
print("\nTask 18:")
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print(f"Task 18 - List with duplicates removed: {unique_list}")

# Task 19
print("\nTask 19:")
sentence = "This is a sample sentence."
words = sentence.split()
word_count = len(words)
print(f"Task 19 - Number of words in the sentence: {word_count}")

# Task 20
print("\nTask 20:")
sum_odd_numbers = 0
for i in range(1, 51, 2):
    sum_odd_numbers += i
print(f"Task 20 - Sum of odd numbers from 1 to 50: {sum_odd_numbers}")

# Task 21
print("\nTask 21:")
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Task 21 - {year} is a leap year")
else:
    print(f"Task 21 - {year} is not a leap year")

# Task 22
print("\nTask 22:")
import math
num = 16
sqrt = math.sqrt(num)
print(f"Task 22 - Square root of {num} is: {sqrt}")

# Task 23
print("\nTask 23:")
import math
num1 = 12
num2 = 18
lcm = (num1 * num2) // math.gcd(num1, num2)
print(f"Task 23 - LCM of {num1} and {num2} is: {lcm}")

# Task 1
print("Task 1:")
num = 5
if num > 0:
    print(f"Task 1 - {num} is positive.")
elif num < 0:
    print(f"Task 1 - {num} is negative.")
else:
    print(f"Task 1 - {num} is zero.")

# Task 2
print("\nTask 2:")
num = 6
if num % 2 == 0:
    print(f"Task 2 - {num} is even.")
else:
    print(f"Task 2 - {num} is odd.")

# Task 3
print("\nTask 3:")
print("Task 3 - Nested if-else statements example:")
x = 10
y = 20
if x > y:
    print("x is greater than y.")
else:
    if x < y:
        print("x is less than y.")
    else:
        print("x and y are equal.")

# Task 4
print("\nTask 4:")
num1 = 12
num2 = 7
num3 = 18
if num1 >= num2 and num1 >= num3:
    print(f"Task 4 - {num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"Task 4 - {num2} is the largest number.")
else:
    print(f"Task 4 - {num3} is the largest number.")

# Task 5
print("\nTask 5:")
num = -9
if num >= 0:
    print(f"Task 5 - Absolute value of {num} is {num}.")
else:
    print(f"Task 5 - Absolute value of {num} is {-num}.")

# Task 6
print("\nTask 6:")
char = 'A'
if char in 'aeiouAEIOU':
    print(f"Task 6 - {char} is a vowel.")
else:
    print(f"Task 6 - {char} is a consonant.")

# Task 7
print("\nTask 7:")
age = 18
if age >= 18:
    print(f"Task 7 - You are eligible to vote.")
else:
    print(f"Task 7 - You are not eligible to vote.")

# Task 8
print("\nTask 8:")
purchase_amount = 100
if purchase_amount >= 1000:
    discount = 0.1 * purchase_amount
    print(f"Task 8 - You get a 10% discount of ${discount}.")
else:
    print("Task 8 - No discount available.")

# Task 9
print("\nTask 9:")
num = 15
if num >= 10 and num <= 20:
    print(f"Task 9 - {num} is within the specified range.")
else:
    print(f"Task 9 - {num} is outside the specified range.")

# Task 10
print("\nTask 10:")
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Task 10 - Your grade is {grade}.")

# Task 11
print("\nTask 11:")
my_string = ""
if my_string:
    print("Task 11 - The string is not empty.")
else:
    print("Task 11 - The string is empty.")

# Task 12
print("\nTask 12:")
a = 3
b = 4
c = 5
if a == b == c:
    triangle_type = "Equilateral"
elif a == b or b == c or a == c:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"
print(f"Task 12 - The triangle is {triangle_type}.")

# Task 13
print("\nTask 13:")
day_num = 2
if day_num == 1:
    day_name = "Sunday"
elif day_num == 2:
    day_name = "Monday"
elif day_num == 3:
    day_name = "Tuesday"
elif day_num == 4:
    day_name = "Wednesday"
elif day_num == 5:
    day_name = "Thursday"
elif day_num == 6:
    day_name = "Friday"
elif day_num == 7:
    day_name = "Saturday"
else:
    day_name = "Invalid Day"
print(f"Task 13 - Day of the week is {day_name}.")

# Task 14
print("\nTask 14:")
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Task 14 - {year} is a leap year.")
else:
    print(f"Task 14 - {year} is not a leap year.")

# Task 15
print("\nTask 15:")
assert 5 > 3, "Assertion error: 5 is not greater than 3."

# Task 16
print("\nTask 16:")
age = 65
if age >= 60:
    print(f"Task 16 - You are eligible for a senior citizen discount.")
else:
    print(f"Task 16 - You are not eligible for a senior citizen discount.")

# Task 17
print("\nTask 17:")
char = 'X'
if char.isupper():
    print(f"Task 17 - {char} is uppercase.")
elif char.islower():
    print(f"Task 17 - {char} is lowercase.")
else:
    print(f"Task 17 - {char} is neither uppercase nor lowercase.")

# Task 18
print("\nTask 18:")
a = 1
b = 2
c = 1
if a == b == c:
    print("Task 18 - The quadratic equation has one real root.")
elif a == b == 0:
    print("Task 18 - The quadratic equation has a linear root.")
else:
    discriminant = b**2 - 4 * a * c
    if discriminant > 0:
        print("Task 18 - The quadratic equation has two real roots.")
    elif discriminant == 0:
        print("Task 18 - The quadratic equation has one real root.")
    else:
        print("Task 18 - The quadratic equation has complex roots.")

# Task 19
print("\nTask 19:")
year = 1900
if year % 100 == 0:
    if year % 400 == 0:
        print(f"Task 19 - {year} is a century year.")
    else:
        print(f"Task 19 - {year} is not a century year.")
else:
    if year % 4 == 0:
        print(f"Task 19 - {year} is a leap year.")
    else:
        print(f"Task 19 - {year} not a leap year")

# Task 20
print("\nTask 20:")
num = 16
sqrt = 4  # Square root of 16 is 4
if num == sqrt**2:
    print(f"Task 20 - {num} is a perfect square.")
else:
    print(f"Task 20 - {num} is not a perfect square.")

# Task 21
print("\nTask 21:")
print("Task 21 - Purpose of 'continue' and 'break' statements in loops:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Task 21 - Odd Number: {i}")
    if i == 5:
        break  # Stop at 5

# Task 22
print("\nTask 22:")
weight = 70  # in kilograms
height = 1.75  # in meters
bmi = weight / (height**2)
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal Weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"Task 22 - Your BMI is {bmi:.2f}, and you are in the category: {category}.")

# Task 23
print("\nTask 23:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(lambda x: x % 2 == 0, numbers)
print(f"Task 23 - Filtered even numbers: {list(filtered_numbers)}")

# Task 24
print("\nTask 24:")
num = 17
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"Task 24 - {num} is a prime number.")
else:
    print(f"Task 24 - {num} is not a prime number.")

# Task 1
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)

print("Task 1 - Squared numbers:", list(squared_numbers))

# Task 2
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)

print("Task 2 - Sum of elements:", result)

# Task 3
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)

print("Task 3 - Product of elements:", product)

# Task 4
names = ["Alice", "Bob", "Charlie"]
uppercase_names = map(str.upper, names)

print("Task 4 - Uppercase names:", list(uppercase_names))

# Task 5
words = ["apple", "banana", "cherry"]
word_lengths = map(len, words)

print("Task 5 - Word lengths:", list(word_lengths))

# Task 6
def add(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = map(add, list1, list2)
print("Task 6 - Sum of elements:", list(result))

# Task 7
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temperatures = [0, 20, 25, 30]
fahrenheit_temperatures = map(celsius_to_fahrenheit, celsius_temperatures)

print("Task 7 - Fahrenheit temperatures:", list(fahrenheit_temperatures))

# Task 8
numbers = [1.5, 2.7, 3.1, 4.9]
rounded_numbers = map(round, numbers)

print("Task 8 - Rounded numbers:", list(rounded_numbers))

# Task 1
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers)

print("Task 1 - Sum of elements:", result)

# Task 2
from functools import reduce

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
product = reduce(multiply, numbers)

print("Task 2 - Product of elements:", product)

# Task 3
numbers = [12, 45, 78, 34, 99, 23]
max_number = reduce(lambda x, y: x if x > y else y, numbers)

print("Task 3 - Maximum element:", max_number)

# Task 4
strings = ["Hello", ", ", "world", "!"]
concatenated_string = reduce(lambda x, y: x + y, strings)

print("Task 4 - Concatenated string:", concatenated_string)

# Task 5
n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))

print("Task 5 - Factorial of", n, ":", factorial)

# Task 6
import math

numbers = [12, 18, 24, 36]
gcd = reduce(math.gcd, numbers)

print("Task 6 - GCD of elements:", gcd)

# Task 7
def sum_of_digits(x, y):
    return int(x) + int(y)

number = "12345"
digit_sum = reduce(sum_of_digits, number)

print("Task 7 - Sum of digits:", digit_sum)



# Task 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(x):
    return x % 2 == 0

even_numbers = filter(is_even, numbers)

print("Task 1 - Even numbers:", list(even_numbers))

# Task 2
names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"]
start_letter = "C"

filtered_names = filter(lambda name: name.startswith(start_letter), names)

print("Task 2 - Names starting with", start_letter + ":", list(filtered_names))

# Task 3
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = filter(is_prime, numbers)

print("Task 3 - Prime numbers:", list(prime_numbers))

# Task 4
values = [1, None, 2, None, 3, None, 4, None, 5]
filtered_values = filter(None, values)

print("Task 4 - Non-None values:", list(filtered_values))

# Task 5
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
min_length = 5

filtered_words = filter(lambda word: len(word) >= min_length, words)

print("Task 5 - Words longer than", min_length, "characters:", list(filtered_words))

# Task 6
threshold = 25
numbers = [12, 30, 45, 15, 8, 50, 60, 70]

filtered_numbers = filter(lambda x: x > threshold, numbers)

print("Task 6 - Numbers greater than", threshold, ":", list(filtered_numbers))

# Task 7
threshold = 25
numbers = [12, 30, 45, 15, 8, 50, 60, 70]

filtered_numbers = filter(lambda x: x > threshold, numbers)

print("Task 7 - Numbers greater than", threshold, ":", list(filtered_numbers))

# Task 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print("Task 2 - Factorial of 5:", result)

# Task 3
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(7)
print("Task 3 - 7th Fibonacci number:", result)

# Task 4
def recursive_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + recursive_sum(numbers[1:])

numbers = [1, 2, 3, 4, 5]
result = recursive_sum(numbers)
print("Task 4 - Sum of elements in [1, 2, 3, 4, 5]:", result)

# Task 6
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

result = gcd(48, 18)
print("Task 6 - GCD of 48 and 18:", result)

# Task 7
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

result = reverse_string("hello")
print("Task 7 - Reverse of 'hello':", result)

# Task 8
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

result = power(2, 3)
print("Task 8 - 2^3:", result)

# Task 9
import itertools

def permutations(s):
    if len(s) == 0:
        return [""]
    else:
        char = s[0]
        rest_permutations = permutations(s[1:])
        result = []
        for perm in rest_permutations:
            for i in range(len(perm) + 1):
                result.append(perm[:i] + char + perm[i:])
        return result

result = permutations("abc")
print("Task 9 - Permutations of 'abc':", result)

# Task 10
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

result = is_palindrome("racecar")
print("Task 10 - Is 'racecar' a palindrome?", result)

# Task 11
def combinations(elements, k):
    if k == 0:
        return [[]]
    if len(elements) == 0:
        return []
    head, tail = elements[0], elements[1:]
    without_head = combinations(tail, k)
    with_head = combinations(tail, k - 1)
    with_head = [[head] + comb for comb in with_head]
    return without_head + with_head

result = combinations([1, 2, 3], 2)
print("Task 11 - Combinations of [1, 2, 3] (2 at a time):", result)

# Task 12
def print_hello():
    print("Hello, World!")

print_hello()

# Task 13
def function_basics(x, y):
    return x + y

result = function_basics(3, 5)
print("Task 13 - Function result:", result)

# Task 14
def function_defaults(x=1, y=2):
    return x * y

result = function_defaults()
print("Task 14 - Function result with defaults:", result)

# Task 15
def function_keyword_args(name, age):
    print("Name:", name)
    print("Age:", age)

function_keyword_args(age=30, name="Alice")

# Task 16
def variable_args(*args):
    for arg in args:
        print(arg)

variable_args("apple", "banana", "cherry")

# Task 17
def keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

keyword_args(name="Bob", age=25, city="New York")

# Task 18
def add(x, y):
    return x + y

result = add(3, 5)
print("Task 18 - Function result:", result)

# Task 19
def outer_function():
    x = 10
    
    def inner_function():
        nonlocal x
        x += 5
        print("Inner function:", x)
    
    inner_function()
    print("Outer function:", x)

outer_function()

# Task 20
square = lambda x: x ** 2
result = square(4)
print("Task 20 - Square of 4:", result)

# Task 21
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
students.sort(key=lambda student: student[1],reverse=True)
print("Task 21 - Students sorted by score:", students)

# Task 22
def higher_order_function(func, numbers):
    result = []
    for number in numbers:
        result.append(func(number))
    return result

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = higher_order_function(square, numbers)
print("Task 22 - Squared numbers:", squared_numbers)

# Task 23
length = len("Hello")
print("Task 23 - Length of 'Hello':", length)

# Task 24
maximum = max(1, 3, 5, 2, 4)
print("Task 24 - Maximum:", maximum)

# Task 25:
minimum = min(1, 3, 5, 2, 4)
print("Task 25 - Minimum:", minimum)

# Task 26
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("Task 26 - Average of numbers:", average)

# Task 27
def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    if count % 2 == 0:
        middle1 = sorted_numbers[count // 2 - 1]
        middle2 = sorted_numbers[count // 2]
        median = (middle1 + middle2) / 2
    else:
        median = sorted_numbers[count // 2]
    return median

numbers = [4, 2, 7, 1, 5]
median = calculate_median(numbers)
print("Task 27 - Median of numbers:", median)

# Task 28
def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    max_count = max(counts.values())
    mode = [number for number, count in counts.items() if count == max_count]
    return mode

numbers = [2, 3, 2, 4, 5, 3, 1, 3]
mode = calculate_mode(numbers)
print("Task 28 - Mode of numbers:", mode)

# Task 29
def calculate_range(numbers):
    """Calculate the range of a list of numbers."""
    return max(numbers) - min(numbers)

numbers = [5, 2, 8, 1, 7]
range_val = calculate_range(numbers)
print("Task 29 - Range of numbers:", range_val)

# Task 30
def calculate_standard_deviation(numbers):
    """Calculate the standard deviation of a list of numbers."""
    import statistics
    return statistics.stdev(numbers)

numbers = [1, 2, 3, 4, 5]
std_deviation = calculate_standard_deviation(numbers)
print("Task 30 - Standard Deviation of numbers:", std_deviation)


