
#Basic variable based questions 
#1. Declare two variables, `x` and `y`, and assign them integer values. Swap the values of these variables without using any temporary variable.
x=11
y=99
print("Before Swap: x={}, y={}".format(x,y))
x=x+y
y=x-y
x=x-y
print("After Swap: x={}, y={}".format(x,y))

#2. Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.
l=int(input("Enter rectangle length:"))
w=int(input("Enter rectangle width:"))
a=l*w
print(f"Area of the rectangle = {a}")

#3. Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.
tc=float(input("Enter temperature in celsius to convert:"))
tf = (tc*9/5)+32
print(f"Temperature in Fahrenheit is {tf}")

#String based questions 
#1. Write a Python program that takes a string as input and prints the length of the string.
s1=input("Enter any string for length:")
print(f"Length of the string is {len(s1)}")

#2. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
s2=input("Enter a sentense to count vowels:")
cnt = 0
for i in s2:
    if i in "aeiou":
        cnt+=1
print(f"No of the vowels are {cnt}")

#3. Given a string, reverse the order of characters using string slicing and print the reversed string.
s3=input("Enter a string to reverse:")
print(f"Reverse string is: {s3[::-1]}")


#4. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).
s4=input("Enter a string to check Palindrome:")
if s4==s4[::-1]:
    print("String is Palindrome")
else:
    print("String is not a Palindrome")

#5. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.
s5=input("Enter string with spaces:")
s55=s5.replace(" ","")
print(f"String witout spaces is: {s55}")