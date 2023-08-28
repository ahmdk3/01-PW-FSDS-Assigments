
#1. Create a list with integers from 1 to 10.
l1=list(range(1,11))
print(f"01 List is {l1}")

#2. Find the length of a list without using the `len()` function.
l2=list(range(1,11))
print(f"02 Length of List is: {l2.index(l2[-1])+1}")

#3. Append an element to the end of a list.
l3=list(range(1,11))
l3.append(11)
print(f"03 Appended List is: {l3}")

#4. Insert an element at a specific index in a list.
i=10
l4=list(range(1,11))
l4.insert(i,11)
print(f"04 Inserted List is: {l4}")

#5. Remove an element from a list by its value.
l5=list(range(1,11))
l5.remove(10)
print(f"05 Removed list is: {l5}")

#6. Remove an element from a list by its index.
i=9
l6=list(range(1,11))
l6.pop(i)
print(f"06 Removed List is: {l6}")

#7. Check if an element exists in a list.
my_list = [10, 20, 30, 40, 50]
element_to_check = 30

if element_to_check in my_list:
    print(f"07 {element_to_check} exists in the list")
else:
    print(f"07 {element_to_check} does not exist in the list")

# Task 8: Find the index of the first occurrence of an element in a list.
my_list = [10, 20, 30, 20, 40]
element_to_find = 20
index = my_list.index(element_to_find)
print(f"08 The index of {element_to_find} is {index}")

# Task 9: Count the occurrences of an element in a list.
count = my_list.count(element_to_find)
print(f"09 The element {element_to_find} occurs {count} times in the list")

# Task 10: Reverse the order of elements in a list.
reversed_list = my_list[::-1]
print("10 Reversed list:", reversed_list)

# Task 11: Sort a list in ascending order.
sorted_ascending = sorted(my_list)
print("11 Ascending order:", sorted_ascending)

# Task 12: Sort a list in descending order.
sorted_descending = sorted(my_list, reverse=True)
print("12 Descending order:", sorted_descending)

# Task 13: Create a list of even numbers from 1 to 20.
even_numbers = [i for i in range(2, 21, 2)]
print("13 Even numbers:", even_numbers)

# Task 14: Create a list of odd numbers from 1 to 20.
odd_numbers = [i for i in range(1, 21, 2)]
print("14 Odd numbers:", odd_numbers)

# Task 15: Find the sum of all elements in a list.
sum_of_elements = sum(my_list)
print("15 Sum of elements:", sum_of_elements)

# Task 16: Find the maximum value in a list.
max_value = max(my_list)
print("16 Maximum value:", max_value)

# Task 17: Find the minimum value in a list.
min_value = min(my_list)
print("17 Minimum value:", min_value)

# Task 18: Create a list of squares of numbers from 1 to 10.
squares = [x ** 2 for x in range(1, 11)]
print("18 Squares:", squares)

# Task 19: Create a list of random numbers.
import random
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("19 Random numbers:", random_numbers)

# Task 20: Remove duplicates from a list.
unique_list = list(set(my_list))
print("20 Unique list:", unique_list)

# Task 21: Find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = list(set(list1) & set(list2))
print("21 Common elements:", common_elements)

# Task 22: Find the difference between two lists.
difference = list(set(list1) - set(list2))
print("22 Difference:", difference)

# Task 23: Merge two lists.
merged_list = list1 + list2
print("23 Merged list:", merged_list)

# Task 24: Multiply all elements in a list by 2.
doubled_list = [x * 2 for x in my_list]
print("24 Doubled list:", doubled_list)

# Task 25: Filter out all even numbers from a list.
filtered_list = [x for x in my_list if x % 2 != 0]
print("25 Filtered list:", filtered_list)

# Task 26: Convert a list of strings to a list of integers.
string_list = ["10", "20", "30", "40"]
integer_list = list(map(int, string_list))
print("26 Integer list:", integer_list)

# Task 27: Convert a list of integers to a list of strings.
stringified_list = list(map(str, my_list))
print("27 Stringified list:", stringified_list)

# Task 28: Flatten a nested list.
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("28 Flattened list:", flattened_list)

# Task 29: Create a list of the first 10 Fibonacci numbers.
def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

fibonacci_list = fibonacci(10)
print("29 Fibonacci list:", fibonacci_list)

# Task 30: Check if a list is sorted.
is_sorted = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
print("30 Is the list sorted:", is_sorted)

# Task 31: Rotate a list to the left by `n` positions.
n = 2
rotated_list = my_list[n:] + my_list[:n]
print("31 Rotated list to the left:", rotated_list)

# Task 32: Rotate a list to the right by `n` positions.
rotated_right_list = my_list[-n:] + my_list[:-n]
print("Rotated list to the right:", rotated_right_list)

# Task 33: Create a list of prime numbers up to 50.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_numbers = [num for num in range(2, 51) if is_prime(num)]
print("Prime numbers:", prime_numbers)

# Task 34: Split a list into chunks of size `n`.
n = 3
chunked_list = [my_list[i:i+n] for i in range(0, len(my_list), n)]
print("Chunked list:", chunked_list)

# Task 35: Find the second largest number in a list.
sorted_list = sorted(my_list)
second_largest = sorted_list[-2]
print("Second largest:", second_largest)

# Task 36: Replace every element in a list with its square.
squared_list = [x ** 2 for x in my_list]
print("Squared list:", squared_list)

# Task 37: Convert a list to a dictionary where list elements become keys and their indices become values.
dict_from_list = {value: index for index, value in enumerate(my_list)}
print("Dictionary from list:", dict_from_list)

# Task 38: Shuffle the elements of a list randomly.
shuffled_list = random.sample(my_list, len(my_list))
print("Shuffled list:", shuffled_list)

# Task 39: Create a list of the first 10 factorial numbers.
import math
factorial_list = [math.factorial(i) for i in range(1, 11)]
print("Factorial list:", factorial_list)

# Task 40: Check if two lists have at least one element in common.
other_list = [40, 50, 60]
have_common_element = any(x in other_list for x in my_list)
print("Do the lists have a common element:", have_common_element)

# Task 41: Remove all elements from a list.
my_list.clear()
print("Empty list:", my_list)

# Task 42: Replace negative numbers in a list with 0.
negative_replaced_list = [max(0, x) for x in my_list]
print("List with negative numbers replaced:", negative_replaced_list)

# Task 43: Convert a string into a list of words.
string = "Hello, how are you?"
word_list = string.split()
print("List of words:", word_list)

# Task 44: Convert a list of words into a string.
list_of_words = ["Hello", "how", "are", "you?"]
string_from_list = " ".join(list_of_words)
print("String from list:", string_from_list)

# Task 45: Create a list of the first `n` powers of 2.
n = 5
powers_of_2 = [2 ** i for i in range(n)]
print("Powers of 2:", powers_of_2)

# Task 46: Find the longest string in a list of strings.
string_list = ["apple", "banana", "cherry", "date"]
longest_string = max(string_list, key=len)
print("Longest string:", longest_string)

# Task 47: Find the shortest string in a list of strings.
shortest_string = min(string_list, key=len)
print("Shortest string:", shortest_string)

# Task 48: Create a list of the first `n` triangular numbers.
def triangular_number(n):
    return (n * (n + 1)) // 2

triangular_numbers = [triangular_number(i) for i in range(1, n + 1)]
print("Triangular numbers:", triangular_numbers)

# Task 49: Check if a list contains another list as a subsequence.
sub_list = [20, 30]
contains_sub_list = any(sub_list == my_list[i:i+len(sub_list)] for i in range(len(my_list) - len(sub_list) + 1))
print("Does the list contain the sub-list:", contains_sub_list)

# Task 50: Swap two elements in a list by their indices.
index1 = 1
index2 = 3
my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
print("List after swapping:", my_list)
