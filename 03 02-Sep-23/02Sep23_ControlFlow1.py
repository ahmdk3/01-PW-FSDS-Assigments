# Question 1
number = float(input("Enter a number: "))
if number > 0:
    print("1. The given number is positive.")
elif number < 0:
    print("1. The given number is negative.")
else:
    print("1. The given number is zero.")

# Question 2
age = int(input("Enter your age: "))
if age >= 18:
    print("2. You are eligible to vote.")
else:
    print("2. You are not eligible to vote.")

# Question 3
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print("3. The maximum number is:", num1)
elif num1 < num2:
    print("3. The maximum number is:", num2)
else:
    print("3. Both numbers are equal.")

# Question 4
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("4. The year is a leap year.")
else:
    print("4. The year is not a leap year.")

# Question 5
character = input("Enter a character: ").lower()
if character.isalpha():
    if character in 'aeiou':
        print("5. The character is a vowel.")
    else:
        print("5. The character is a consonant.")
else:
    print("5. Invalid input.")

# Question 6
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("6. The number is even.")
else:
    print("6. The number is odd.")

# Question 7
def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num

number = float(input("Enter a number: "))
result = absolute_value(number)
print("7. The absolute value of", number, "is", result)

# Question 8
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("8. The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("8. The largest number is:", num2)
else:
    print("8. The largest number is:", num3)

# Question 9
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print("9. The string is a palindrome.")
else:
    print("9. The string is not a palindrome.")

# Question 10
score = float(input("Enter the student's score: "))
if score >= 90:
    print("10. The grade is A.")
elif score >= 80:
    print("10. The grade is B.")
elif score >= 70:
    print("10. The grade is C.")
elif score >= 60:
    print("10. The grade is D.")
else:
    print("10. The grade is F.")

# Question 11
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2:
    if num1 >= num3:
        print("11. The largest number is:", num1)
    else:
        print("11. The largest number is:", num3)
else:
    if num2 >= num3:
        print("11. The largest number is:", num2)
    else:
        print("11. The largest number is:", num3)

# Question 12
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 == side2 == side3:
    print("12. The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("12. The triangle is isosceles.")
else:
    print("12. The triangle is scalene.")

# Question 13
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("13. The year is a leap year and a century year.")
        else:
            print("13. The year is not a leap year but a century year.")
    else:
        print("13. The year is a leap year but not a century year.")
else:
    print("13. The year is neither a leap year nor a century year.")

# Question 14
num = float(input("Enter a number: "))
if num > 0:
    print("14. The number is positive.")
elif num < 0:
    print("14. The number is negative.")
else:
    print("14. The number is zero.")

# Question 15
age = int(input("Enter your age: "))
if age >= 13 and age <= 19:
    print("15. You are a teenager.")
else:
    print("15. You are not a teenager.")

# Question 16
angle = float(input("Enter the angle measure (in degrees): "))
if angle < 90:
    print("16. The angle is acute.")
elif angle == 90:
    print("16. The angle is right.")
else:
    print("16. The angle is obtuse.")

# Question 17
import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("17. The roots are real and distinct. Root 1 =", root1, "Root 2 =", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("17. The root is real and equal. Root =", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("17. The roots are complex. Root 1 =", real_part, "+", imaginary_part, "i, Root 2 =", real_part, "-", imaginary_part, "i")

# Question 18
day_number = int(input("Enter a number (1 for Monday, 2 for Tuesday, etc.): "))
if day_number == 1:
    print("18. The day is Monday.")
elif day_number == 2:
    print("18. The day is Tuesday.")
elif day_number == 3:
    print("18. The day is Wednesday.")
elif day_number == 4:
    print("18. The day is Thursday.")
elif day_number == 5:
    print("18. The day is Friday.")
elif day_number == 6:
    print("18. The day is Saturday.")
elif day_number == 7:
    print("18. The day is Sunday.")
else:
    print("18. Invalid input.")

# Question 19
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("19. The year is a leap year.")
else:
    print("19. The year is not a leap year.")

# Question 20
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("20. The number is prime.")
else:
    print("20. The number is not prime.")

# Question 21
score = float(input("Enter the score: "))
if score >= 90:
    print("21. Grade: A")
elif score >= 80:
    print("21. Grade: B")
elif score >= 70:
    print("21. Grade: C")
elif score >= 60:
    print("21. Grade: D")
else:
    print("21. Grade: F")

# Question 22
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
if angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("22. It is a right triangle.")
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("22. It is an acute triangle.")
    else:
        print("22. It is an obtuse triangle.")
else:
    print("22. It is not a valid triangle.")

# Question 23
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("23. BMI Category: Underweight")
elif 18.5 <= bmi < 24.9:
    print("23. BMI Category: Normal")
elif 24.9 <= bmi < 29.9:
    print("23. BMI Category: Overweight")
else:
    print("23. BMI Category: Obese")

# Question 24
number = float(input("Enter a number: "))
if number > 0:
    print("24. The number is positive.")
elif number < 0:
    print("24. The number is negative.")
else:
    print("24. The number is zero.")

# Question 25
character = input("Enter a character: ")
if character.isalpha():
    if character.isupper():
        print("25. The character is uppercase.")
    elif character.islower():
        print("25. The character is lowercase.")
    else:
        print("25. The character is neither uppercase nor lowercase.")
else:
    print("25. The character is special.")

# Question 26
purchase_amount = float(input("Enter the purchase amount: "))
discount = 0
if purchase_amount >= 1000:
    discount = 0.1
elif purchase_amount >= 500:
    discount = 0.05
final_amount = purchase_amount - (purchase_amount * discount)
print("26. Discount:", discount * 100, "%")
print("26. Final amount:", final_amount)

# Question 27
units_consumed = float(input("Enter the units consumed: "))
total_cost = 0
if units_consumed <= 50:
    total_cost = units_consumed * 2.5
elif units_consumed <= 150:
    total_cost = 50 * 2.5 + (units_consumed - 50) * 3.0
elif units_consumed <= 250:
    total_cost = 50 * 2.5 + 100 * 3.0 + (units_consumed - 150) * 3.5
else:
    total_cost = 50 * 2.5 + 100 * 3.0 + 100 * 3.5 + (units_consumed - 250) * 4.0
print("27. Total electricity bill:", total_cost)

# Question 28
angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))
angle3 = int(input("Enter the third angle: "))
if angle1 + angle2 + angle3 == 360:
    if angle1 == angle2 == angle3 == 90:
        print("28. It is a square.")
    elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
        print("28. It is a rectangle.")
    else:
        print("28. It is a quadrilateral.")
else:
    print("28. It is not a valid quadrilateral.")

# Question 29
month = int(input("Enter a month (1-12): "))
if 1 <= month <= 12:
    if 3 <= month <= 5:
        print("29. The season is spring.")
    elif 6 <= month <= 8:
        print("29. The season is summer.")
    elif 9 <= month <= 11:
        print("29. The season is autumn.")
    else:
        print("29. The season is winter.")
else:
    print("29. Invalid input.")

# Question 30
year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("30. The year is a leap year.")
else:
    print("30. The year is not a leap year.")
if month in [4, 6, 9, 11]:
    print("30. The month has 30 days.")
elif month != 2:
    print("30. The month has 31 days.")
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("30. The month has 29 days.")
    else:
        print("30. The month has 28 days.")
