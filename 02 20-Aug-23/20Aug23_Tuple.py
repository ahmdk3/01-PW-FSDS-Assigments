# 1. Create a tuple with integers from 1 to 5.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# 2. Access the third element of a tuple.
third_element = my_tuple[2]
print(third_element)

# 3. Find the length of a tuple without using the `len()` function.
tuple_length = sum(1 for _ in my_tuple)
print(tuple_length)

# 4. Count the occurrences of an element in a tuple.
element_count = my_tuple.count(3)
print(element_count)

# 5. Find the index of the first occurrence of an element in a tuple.
index_of_element = my_tuple.index(3)
print(index_of_element)

# 6. Check if an element exists in a tuple.
element_exists = 3 in my_tuple
print(element_exists)

# 7. Convert a tuple to a list.
my_list = list(my_tuple)
print(my_list)

# 8. Convert a list to a tuple.
my_new_tuple = tuple(my_list)
print(my_new_tuple)

# 9. Unpack the elements of a tuple into variables.
a, b, c, d, e = my_tuple
print(a, b, c, d, e)

# 10. Create a tuple of even numbers from 1 to 10.
even_numbers = tuple(range(2, 11, 2))
print(even_numbers)

# 11. Create a tuple of odd numbers from 1 to 10.
odd_numbers = tuple(range(1, 11, 2))
print(odd_numbers)

# 12. Concatenate two tuples.
concatenated_tuple = my_tuple + even_numbers
print(concatenated_tuple)

# 13. Repeat a tuple three times.
repeated_tuple = my_tuple * 3
print(repeated_tuple)

# 14. Check if a tuple is empty.
is_empty = not my_tuple
print(is_empty)

# 15. Create a nested tuple.
nested_tuple = (my_tuple, even_numbers)
print(nested_tuple)

# 16. Access the first element of a nested tuple.
first_element_nested = nested_tuple[0]
print(first_element_nested)

# 17. Create a tuple with a single element.
single_element_tuple = (42,)
print(single_element_tuple)

# 18. Compare two tuples.
are_equal = my_tuple == even_numbers
print(are_equal)

# 19. Delete a tuple. (You can't delete elements from a tuple, but you can remove the reference to it.)
del my_tuple

# 20. Slice a tuple.
sliced_tuple = my_new_tuple[1:4]
print(sliced_tuple)

# 21. Find the maximum value in a tuple.
max_value = max(my_new_tuple)
print(max_value)

# 22. Find the minimum value in a tuple.
min_value = min(my_new_tuple)
print(min_value)

# 23. Convert a string to a tuple of characters.
string_to_tuple = tuple("Hello")
print(string_to_tuple)

# 24. Convert a tuple of characters to a string.
tuple_to_string = ''.join(string_to_tuple)
print(tuple_to_string)

# 25. Create a tuple from multiple data types.
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# 26. Check if two tuples are identical.
are_identical = my_new_tuple == my_list
print(are_identical)

# 27. Sort the elements of a tuple.
sorted_tuple = tuple(sorted(my_new_tuple))
print(sorted_tuple)

# 28. Convert a tuple of integers to a tuple of strings.
tuple_of_integers = (1, 2, 3)
tuple_of_strings = tuple(str(x) for x in tuple_of_integers)
print(tuple_of_strings)

# 29. Convert a tuple of strings to a tuple of integers.
tuple_of_strings = ('1', '2', '3')
tuple_of_integers = tuple(int(x) for x in tuple_of_strings)
print(tuple_of_integers)

# 30. Merge two tuples.
merged_tuple = my_new_tuple + even_numbers
print(merged_tuple)

# 31. Flatten a nested tuple.
flattened_tuple = tuple(item for sublist in nested_tuple for item in sublist)
print(flattened_tuple)

# 32. Create a tuple of the first 5 prime numbers.
prime_numbers = (2, 3, 5, 7, 11)
print(prime_numbers)

# 33. Check if a tuple is a palindrome.
is_palindrome = my_new_tuple == my_new_tuple[::-1]
print(is_palindrome)

# 34. Create a tuple of squares of numbers from 1 to 5.
squares_tuple = tuple(x ** 2 for x in range(1, 6))
print(squares_tuple)

# 35. Filter out all even numbers from a tuple.
filtered_tuple = tuple(x for x in my_new_tuple if x % 2 != 0)
print(filtered_tuple)

# 36. Multiply all elements in a tuple by 2.
multiplied_tuple = tuple(x * 2 for x in my_new_tuple)
print(multiplied_tuple)

# 37. Create a tuple of random numbers.
import random
random_tuple = tuple(random.randint(1, 100) for _ in range(5))
print(random_tuple)

# 38. Check if a tuple is sorted.
is_sorted = tuple(sorted(my_new_tuple)) == my_new_tuple
print(is_sorted)

# 39. Rotate a tuple to the left by `n` positions.
n = 2
rotated_left_tuple = my_new_tuple[n:] + my_new_tuple[:n]
print(rotated_left_tuple)

# 40. Rotate a tuple to the right by `n` positions.
rotated_right_tuple = my_new_tuple[-n:] + my_new_tuple[:-n]
print(rotated_right_tuple)

# 41. Create a tuple of the first 5 Fibonacci numbers.
fibonacci_tuple = (0, 1, 1, 2, 3)
print(fibonacci_tuple)

# 42. Create a tuple from user input.
user_input = input("Enter comma-separated values: ")
user_tuple = tuple(map(int, user_input.split(',')))
print(user_tuple)

# 43. Swap two elements in a tuple.
tuple_list = list(my_new_tuple)
tuple_list[1], tuple_list[3] = tuple_list[3], tuple_list[1]
swapped_tuple = tuple(tuple_list)
print(swapped_tuple)

# 44. Reverse the elements of a tuple.
reversed_tuple = my_new_tuple[::-1]
print(reversed_tuple)

# 45. Create a tuple of the first `n` powers of 2.
n = 5
powers_of_2_tuple = tuple(2 ** i for i in range(1, n+1))
print(powers_of_2_tuple)

# 46. Find the longest string in a tuple of strings.
strings_tuple = ('apple', 'banana', 'cherry')
longest_string = max(strings_tuple, key=len)
print(longest_string)

# 47. Find the shortest string in a tuple of strings.
shortest_string = min(strings_tuple, key=len)
print(shortest_string)

# 48. Create a tuple of the first `n` triangular numbers.
n = 5
triangular_numbers = tuple((i * (i + 1)) // 2 for i in range(1, n+1))
print(triangular_numbers)

# 49. Check if a tuple contains another tuple as a subsequence.
contains_subtuple = any(all(x in my_new_tuple for x in subtuple) for subtuple in [(2, 3), (4, 5)])
print(contains_subtuple)

# 50. Create a tuple of alternating 1s and 0s of length `n`.
n = 6
alternating_tuple = tuple(1 if i % 2 == 0 else 0 for i in range(n))
print(alternating_tuple)

