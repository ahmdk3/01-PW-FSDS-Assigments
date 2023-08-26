## String Assigment

#1. Write a program to reverse a string.
s1=input('Input a string:')
print(f"01 Reverse String is: '{s1[::-1]}'")
#2. Check if a string is a palindrome.
s2=s1
if s2==s2[::-1]:
    print(f"02 '{s2}' is palindrome.")
else:
    print(f"02 '{s2}' is not a palindrome.")
#3. Convert a string to uppercase.
s3=s1
print(f"03 Upper case string is '{s3.upper()}'")
#4. Convert a string to lowercase.
s4=s1
print(f"04 Lower case string is '{s4.lower()}'")
#5. Count the number of vowels in a string.
s5=s1
count=0
for i in s5:
    if i in 'aeiou':
        count+=1
print(f"05 Vowels count is: {count}")
#6. Count the number of consonants in a string.
s6=s1
count=0
for i in s6:
    if i not in 'aeiou ':
        count+=1
print(f"06 Consonants count is: {count}")
#7. Remove all whitespaces from a string.
s7=s1
print(f"07 Removed whitespaces from string is '{s7.replace(' ','')}'")

#8. Find the length of a string without using the `len()` function.
s8=s1
count=0
for i in s8:
    count+=1
print(f"08 Length of string is: {count}")

#9. Check if a string contains a specific word.
s9=s1
wrd='string'
if wrd in s9:
    print(f"09 '{wrd}' contains in '{s9}'")
else:
    print(f"09 '{wrd}' does not contains in '{s9}'")
#10. Replace a word in a string with another word.
s10=s1
rplc='home'
print(f"10 Replaced String is:'{s10.replace(wrd,rplc)}'")

#11. Count the occurrences of a word in a string.
s11=s1
count=s11.count(wrd)
print(f"11 '{wrd}' occured {count} time in '{s11}'")
#12. Find the first occurrence of a word in a string.
s12=s1
idx=s12.find(wrd)
print(f"12 '{wrd}' found at index {idx} in '{s12}'")

#13. Find the last occurrence of a word in a string.
s13=s1
idx=s13.rfind(wrd)
print(f"13 '{wrd}' found at index {idx} in '{s12}'")

#14. Split a string into a list of words.
s14=s1
print(f"14 Split words are: {s14.split()}")
#15. Join a list of words into a string.
s15=s1.split()
print(f"15 Joined word for '{s15}' is '{' '.join(s15)}'")

#16. Convert a string where words are separated by spaces to one where words are separated by underscores.
s16=s1
print(f"16 Spaced words '{s16}' converted to '{'_'.join(s16.split())}'")

#17. Check if a string starts with a specific word or phrase.
s17=s1
if s17.startswith(wrd):
    print(f"17 '{wrd}' starts with in '{s17}'")
else:
    print(f"17 '{wrd}' doesn't starts with in '{s17}'")

#18. Check if a string ends with a specific word or phrase.
s18=s1
if s18.endswith(wrd):
    print(f"18 '{wrd}' starts with in '{s18}'")
else:
    print(f"18 '{wrd}' doesn't starts with in '{s18}'")

#19. Convert a string to title case (e.g., "hello world" to "Hello World").
s19=s1
print(f"19 {s19} in title case is: '{s19.title()}'")

#20. Find the longest word in a string.
s20=s1
lng=''
for wrd in s20.split():
    if len(wrd)>len(lng):
        lng=wrd
print(f"20 Longest word in '{s20}' is '{lng}'")

#21. Find the shortest word in a string.
s21=s1
shrt=s21.split()[0]
for word in s21.split():
    if len(word)<len(shrt):
        shrt=word
print(f"21 Shortest word in '{s21}' is '{shrt}'")

#22. Reverse the order of words in a string.
s22=s1
rev=" ".join(s22.split()[::-1])
print(f"22 Reversed word order of '{s22}' is '{rev}'")

#23. Check if a string is alphanumeric.
s23=s1
if s23.isalnum():
    print(f"23 '{s23}' is Alphanumeric")
else:
    print(f"23 '{s23}' is not a Alphanumeric")

#24. Extract all digits from a string.
s24=s1
dgt=''
for char in s24:
    if char.isdigit():
        dgt+=char
print(f"24 Extracted digits from '{s24}' are '{dgt}'")

#25. Extract all alphabets from a string.
s25=s1
alph=''
for char in s25:
    if char.isalpha():
        alph+=char
print(f"25 Extracted alphabets from '{s25}' are '{alph}'")

#26. Count the number of uppercase letters in a string.
s26=s1
count=0
for char in s26:
    if char.isupper():
        count+=1
print(f"26 Number of Upper letters are: {count}")

#27. Count the number of lowercase letters in a string.
s27=s1
count=0
for char in s27:
    if char.islower():
        count+=1
print(f"27 Number of Lower letters are: {count}")

#28. Swap the case of each character in a string.
s28=s1
swapped=''
for char in s28:
    if char.islower():
        swapped=swapped+char.upper()
    elif char.isupper():
        swapped=swapped+char.lower()
    else:
        swapped=swapped+char
print(f"28 Swapped Upper Lower case string is: {swapped}")

#29. Remove a specific word from a string.
#30. Check if a string is a valid email address.
#31. Extract the username from an email address string.
#32. Extract the domain name from an email address string.
#33. Replace multiple spaces in a string with a single space.
#34. Check if a string is a valid URL.
#35. Extract the protocol (http or https) from a URL string.
#36. Find the frequency of each character in a string.
#37. Remove all punctuation from a string.
#38. Check if a string contains only digits.
#39. Check if a string contains only alphabets.
#40. Convert a string to a list of characters.
#41. Check if two strings are anagrams.
#42. Encode a string using a Caesar cipher.
#43. Decode a Caesar cipher encoded string.
#44. Find the most frequent word in a string.
#45. Find all unique words in a string.
#46. Count the number of syllables in a string.
#47. Check if a string contains any special characters.
#48. Remove the nth word from a string.
#49. Insert a word at the nth position in a string.
#50. Convert a CSV string to a list of lists.