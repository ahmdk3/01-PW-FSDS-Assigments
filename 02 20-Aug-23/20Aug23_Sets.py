# 1. Create a set with integers from 1 to 5.
set1 = set(range(1, 6))
print("1. Set with integers from 1 to 5:", set1)

# 2. Add an element to a set.
set1.add(6)
print("2. Element added to the set:", set1)

# 3. Remove an element from a set.
set1.remove(3)
print("3. Element removed from the set:", set1)

# 4. Check if an element exists in a set.
element_exists = 4 in set1
print("4. Element 4 exists in the set:", element_exists)

# 5. Find the length of a set without using the `len()` function.
set_length = sum(1 for _ in set1)
print("5. Length of the set:", set_length)

# 6. Clear all elements from a set.
set1.clear()
print("6. Set cleared:", set1)

# 7. Create a set of even numbers from 1 to 10.
even_numbers = set(range(2, 11, 2))
print("7. Set of even numbers from 1 to 10:", even_numbers)

# 8. Create a set of odd numbers from 1 to 10.
odd_numbers = set(range(1, 11, 2))
print("8. Set of odd numbers from 1 to 10:", odd_numbers)

# 9. Find the union of two sets.
union_set = even_numbers.union(odd_numbers)
print("9. Union of two sets:", union_set)

# 10. Find the intersection of two sets.
intersection_set = even_numbers.intersection(odd_numbers)
print("10. Intersection of two sets:", intersection_set)

# 11. Find the difference between two sets.
difference_set = even_numbers.difference(odd_numbers)
print("11. Difference between two sets:", difference_set)

# 12. Check if a set is a subset of another set.
is_subset = even_numbers.issubset(union_set)
print("12. Even numbers set is a subset of union set:", is_subset)

# 13. Check if a set is a superset of another set.
is_superset = union_set.issuperset(even_numbers)
print("13. Union set is a superset of even numbers set:", is_superset)

# 14. Create a set from a list.
my_list = [1, 2, 3, 4, 5]
set_from_list = set(my_list)
print("14. Set from a list:", set_from_list)

# 15. Convert a set to a list.
list_from_set = list(set_from_list)
print("15. List from set:", list_from_set)

# 16. Remove a random element from a set.
import random
random_element = random.sample(set_from_list, 1)[0]
set_from_list.remove(random_element)
print("16. Random element removed from the set:", set_from_list)

# 17. Pop an element from a set.
popped_element = set_from_list.pop()
print("17. Element popped from the set:", popped_element)

# 18. Check if two sets have no elements in common.
no_common_elements = not set1.isdisjoint(odd_numbers)
print("18. No common elements between set1 and odd numbers set:", no_common_elements)

# 19. Find the symmetric difference between two sets.
symmetric_difference = even_numbers.symmetric_difference(odd_numbers)
print("19. Symmetric difference between two sets:", symmetric_difference)

# 20. Update a set with elements from another set.
set1.update(even_numbers)
print("20. Set1 updated with even numbers:", set1)

# 21. Create a set of the first 5 prime numbers.
prime_numbers = {2, 3, 5, 7, 11}
print("21. Set of the first 5 prime numbers:", prime_numbers)

# 22. Check if two sets are identical.
are_identical = set_from_list == list_from_set
print("22. Sets from list and list from set are identical:", are_identical)

# 23. Create a frozen set.
frozen_set = frozenset(set_from_list)
print("23. Frozen set:", frozen_set)

# 24. Check if a set is disjoint with another set.
is_disjoint = set1.isdisjoint(odd_numbers)
print("24. Set1 is disjoint with odd numbers set:", is_disjoint)

# 25. Create a set of squares of numbers from 1 to 5.
squares_set = {x ** 2 for x in range(1, 6)}
print("25. Set of squares of numbers from 1 to 5:", squares_set)

# 26. Filter out all even numbers from a set.
filtered_set = {x for x in set1 if x % 2 != 0}
print("26. Filtered set with odd numbers:", filtered_set)

# 27. Multiply all elements in a set by 2.
set1 = {x * 2 for x in set1}
print("27. Set with elements multiplied by 2:", set1)

# 28. Create a set of random numbers.
random_set = {random.randint(1, 100) for _ in range(5)}
print("28. Set of random numbers:", random_set)

# 29. Check if a set is empty.
is_empty = not set1
print("29. Is set1 empty:", is_empty)

# 30. Create a nested set (hint: use frozenset).
nested_set = {frozenset({1, 2}), frozenset({3, 4})}
print("30. Nested set:", nested_set)

# 31. Remove an element from a set using the discard method.
set1.discard(4)
print("31. Element 4 removed using discard method:", set1)

# 32. Compare two sets.
are_equal = set1 == odd_numbers
print("32. Set1 and odd numbers set are equal:", are_equal)

# 33. Create a set from a string.
string_set = set("Hello")
print("33. Set from a string:", string_set)

# 34. Convert a set of strings to a set of integers.
string_set = {"1", "2", "3"}
int_set = {int(x) for x in string_set}
print("34. Set of integers from a set of strings:", int_set)

# 35. Convert a set of integers to a set of strings.
int_set = {1, 2, 3}
string_set = {str(x) for x in int_set}
print("35. Set of strings from a set of integers:", string_set)

# 36. Create a set from a tuple.
my_tuple = (1, 2, 3, 4, 5)
set_from_tuple = set(my_tuple)
print("36. Set from a tuple:", set_from_tuple)

# 37. Convert a set to a tuple.
tuple_from_set = tuple(set_from_tuple)
print("37. Tuple from a set",tuple_from_set)

# 38. Find the maximum value in a set.
max_value = max(set_from_tuple)
print("38. Maximum value in the set:", max_value)

# 39. Find the minimum value in a set.
min_value = min(set_from_tuple)
print("39. Minimum value in the set:", min_value)

# 40. Create a set from user input.
user_input = input("Enter comma-separated values: ")
user_set = set(map(int, user_input.split(',')))
print("40. Set from user input:", user_set)

# 41. Check if the intersection of two sets is empty.
intersection_empty = len(set1.intersection(even_numbers)) == 0
print("41. Intersection of set1 and even numbers set is empty:", intersection_empty)

# 42. Create a set of the first 5 Fibonacci numbers.
fibonacci_set = {0, 1, 1, 2, 3}
print("42. Set of the first 5 Fibonacci numbers:", fibonacci_set)

# 43. Remove duplicates from a list using sets.
duplicated_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(duplicated_list)
print("43. List with duplicates removed:", list(unique_set))

# 44. Check if two sets have the same elements, regardless of their count.
same_elements = set1 == unique_set
print("44. Set1 and unique set have the same elements:", same_elements)

# 45. Create a set of the first `n` powers of 2.
n = 5
powers_of_2_set = {2 ** i for i in range(1, n+1)}
print("45. Set of the first", n, "powers of 2:", powers_of_2_set)

# 46. Find the common elements between a set and a list.
common_elements = set1.intersection(duplicated_list)
print("46. Common elements between set1 and duplicated list:", common_elements)

# 47. Create a set of the first `n` triangular numbers.
n = 5
triangular_numbers_set = {(i * (i + 1)) // 2 for i in range(1, n+1)}
print("47. Set of the first", n, "triangular numbers:", triangular_numbers_set)

# 48. Check if a set contains another set as a subset.
contains_subset = even_numbers.issubset(set1)
print("48. Even numbers set is a subset of set1:", contains_subset)

# 49. Create a set of alternating 1s and 0s of length `n`.
n = 6
alternating_set = {1 if i % 2 == 0 else 0 for i in range(n)}
print("49. Set of alternating 1s and 0s of length", n, ":", alternating_set)

# 50. Merge multiple sets into one.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = {5, 6, 7}
merged_set = set_a.union(set_b, set_c)
print("50. Merged set from set_a, set_b, and set_c:", merged_set)


