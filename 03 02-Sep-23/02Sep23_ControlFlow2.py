

# Intermediate Level:

# Question 11
import math
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("11. The roots are real and distinct. Root 1 =", root1, "Root 2 =", root2)
elif discriminant == 0:
    root = -b / (2*a)
    print("11. The root is real and equal. Root =", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("11. The roots are complex. Root 1 =", real_part, "+", imaginary_part, "i, Root 2 =", real_part, "-", imaginary_part, "i")

# Question 12
day_number = int(input("Enter a number (1 for Monday, 2 for Tuesday, etc.): "))
if day_number == 1:
    print("12. The day is Monday.")
elif day_number == 2:
    print("12. The day is Tuesday.")
elif day_number == 3:
    print("12. The day is Wednesday.")
elif day_number == 4:
    print("12. The day is Thursday.")
elif day_number == 5:
    print("12. The day is Friday.")
elif day_number == 6:
    print("12. The day is Saturday.")
elif day_number == 7:
    print("12. The day is Sunday.")
else:
    print("12. Invalid input.")

# Question 13
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
if num < 0:
    print("13. Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print("13. The factorial of", num, "is", result)

# Question 14
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3
print("14. The largest number is:", largest)

# Question 15
print("15. ATM Transaction Menu")
print("1. Deposit")
print("2. Withdraw")
print("3. Balance Inquiry")
choice = int(input("Enter your choice (1/2/3): "))
if choice == 1:
    print("You selected: Deposit")
elif choice == 2:
    print("You selected: Withdraw")
elif choice == 3:
    print("You selected: Balance Inquiry")
else:
    print("Invalid choice")

# Question 16
def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    if s == s[::-1]:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print("16. The string is a palindrome.")
else:
    print("16. The string is not a palindrome.")

# Question 17
numbers = []
for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

numbers.sort()
sum_without_extremes = sum(numbers[1:-1])
average = sum_without_extremes / 3
print("17. The average of the numbers excluding the smallest and largest is:", average)

# Question 18
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("18. Temperature in Fahrenheit:", fahrenheit)

# Question 19
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("19. Calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))

if choice in [1, 2, 3, 4]:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if choice == 1:
        result = add(num1, num2)
        operation = "Addition"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "Division"
    
    print(f"19. {operation} result: {result}")
else:
    print("19. Invalid choice")

# Question 20
import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))

p = -b / (3 * a)
q = p ** 3 + (b * c - 3 * a * d) / (6 * a ** 2)

root1 = p + cmath.sqrt(q)
root2 = p - cmath.sqrt(q)

print("20. Root 1:", root1)
print("20. Root 2:", root2)

# Advanced Level:

# Question 21
income = float(input("Enter your income: "))
if income <= 10000:
    tax = 0.0
elif income <= 50000:
    tax = 0.1 * (income - 10000)
else:
    tax = 0.1 * 40000 + 0.2 * (income - 50000)
print(f"21. Income tax: {tax}")

# Question 22
import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

if user_choice not in choices:
    print("Invalid choice.")
else:
    print("22. Computer's choice:", computer_choice)
    print("22. Your choice:", user_choice)

    if computer_choice == user_choice:
        print("22. It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("22. You win!")
    else:
        print("22. Computer wins!")

# Question 23
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the password length: "))
use_uppercase = input("Include uppercase letters (yes/no): ").lower() == "yes"
use_digits = input("Include digits (yes/no): ").lower() == "yes"
use_special_chars = input("Include special characters (yes/no): ").lower() == "yes"

if length < 1:
    print("Invalid password length.")
else:
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    print(f"23. Generated password: {password}")

# Question 24
import random

def text_adventure():
    print("24. Text Adventure Game")
    print("You find yourself in a dark forest. There are three paths ahead of you.")
    choice = input("Choose a path (1/2/3): ")

    if choice == "1":
        print("You follow the path and find a hidden treasure chest!")
    elif choice == "2":
        print("You encounter a group of friendly forest animals.")
    elif choice == "3":
        print("You stumble upon a spooky abandoned house.")
    else:
        print("Invalid choice. The adventure ends.")

text_adventure()

# Question 25
def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions (identity)"
        else:
            return "No solution (contradiction)"
    else:
        x = -b / a
        return x

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
result = solve_linear_equation(a, b)
print("25. Solution for x:", result)

# Question 26
def quiz_game():
    questions = [
        {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris"], "correct_answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Earth"], "correct_answer": "Mars"},
        {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Giraffe"], "correct_answer": "Blue Whale"}
    ]

    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")
        
        answer = input("Your answer (1/2/3): ")
        if answer == str(q['options'].index(q['correct_answer']) + 1):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {q['correct_answer']}\n")
    
    print(f"Your score: {score}/{len(questions)}")

quiz_game()

# Question 27
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print("27. The number is prime.")
else:
    print("27. The number is not prime.")

# Question 28
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 <= num2 and num1 <= num3:
    smallest = num1
    if num2 <= num3:
        middle = num2
        largest = num3
    else:
        middle = num3
        largest = num2
elif num2 <= num1 and num2 <= num3:
    smallest = num2
    if num1 <= num3:
        middle = num1
        largest = num3
    else:
        middle = num3
        largest = num1
else:
    smallest = num3
    if num1 <= num2:
        middle = num1
        largest = num2
    else:
        middle = num2
        largest = num1

print(f"28. Numbers in ascending order: {smallest}, {middle}, {largest}")

# Question 29
def solve_quartic(a, b, c, d, e, x):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e

def find_roots_quartic(a, b, c, d, e):
    roots = []
    for x in range(-1000, 1001):
        if solve_quartic(a, b, c, d, e, x) == 0:
            roots.append(x)
    return roots

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))
e = float(input("Enter coefficient e: "))

quartic_roots = find_roots_quartic(a, b, c, d, e)
if len(quartic_roots) > 0:
    print("29. Roots of the quartic equation:", quartic_roots)
else:
    print("29. No real roots found.")

# Question 30
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi)

print(f"30. Your BMI is {bmi:.2f}, which falls into the category: {bmi_category}")

# Challenge Level:

# Question 31
def validate_password(password):
    if len(password) < 8:
        return "Password is too short (min 8 characters)"
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter"
    if not any(char in string.punctuation for char in password):
        return "Password must contain at least one special character"

    return "Password is valid"

password = input("Enter a password: ")
validation_result = validate_password(password)
print(f"31. {validation_result}")

# Question 32
def matrix_addition(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_subtraction(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    return result

print("32. Matrix Operations")
print("1. Matrix Addition")
print("2. Matrix Subtraction")
operation_choice = int(input("Choose an operation (1/2): "))

if operation_choice == 1:
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = matrix_addition(matrix1, matrix2)
    print(f"Matrix Addition Result: {result}")
elif operation_choice == 2:
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = matrix_subtraction(matrix1, matrix2)
    print(f"Matrix Subtraction Result: {result}")
else:
    print("Invalid choice")

# Question 33
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print(f"33. The greatest common divisor (GCD) of {num1} and {num2} is {result}")

# Question 34
def matrix_multiplication(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_multiplication(matrix1, matrix2)
print(f"34. Matrix Multiplication Result: {result}")

# Question 35
def print_board(board):
    for row in board:
        print(' | '.join(row))
        if row != board[-1]:
            print('---------')

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if is_valid_move(board, row, col):
            board[row][col] = current_player
            if is_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

print("35. Let's play Tic-Tac-Toe!")
play_tic_tac_toe()

# Question 36
def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
fibonacci_sequence = generate_fibonacci(n)
print(f"36. Fibonacci Sequence ({n} terms): {fibonacci_sequence}")

# Question 37
def calculate_nth_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    result = calculate_nth_fibonacci(n - 1, memo) + calculate_nth_fibonacci(n - 2, memo)
    memo[n] = result
    return result

n = int(input("Enter the term number to calculate in the Fibonacci sequence: "))
fibonacci_value = calculate_nth_fibonacci(n)
print(f"37. The {n}th term in the Fibonacci sequence is: {fibonacci_value}")

# Question 38
import calendar
def generate_calendar(year, month):
    import calendar
    cal = calendar.month(year, month)
    return cal

year = int(input("Enter a year: "))
month = int(input("Enter a month (1-12): "))
calendar_month = generate_calendar(year, month)
print(f"38. Calendar for {calendar.month_name[month]} {year}:\n{calendar_month}")

# Question 39
import random

def simulate_blackjack():
    def draw_card():
        return random.randint(1, 11)

    player_score = draw_card() + draw_card()
    computer_score = draw_card()

    print("39. Let's play Blackjack!")
    print(f"You have: {player_score}")
    while player_score < 21:
        choice = input("Do you want to 'Hit' or 'Stand'? ").lower()
        if choice == 'hit':
            card = draw_card()
            player_score += card
            print(f"You drew a {card}. Your score: {player_score}")
        elif choice == 'stand':
            break
        else:
            print("Invalid choice. Please enter 'Hit' or 'Stand'.")

    while computer_score < 17:
        card = draw_card()
        computer_score += card

    print(f"Computer has: {computer_score}")

    if player_score > 21:
        return "You busted. Computer wins!"
    elif computer_score > 21:
        return "Computer busted. You win!"
    elif player_score > computer_score:
        return "You win!"
    elif computer_score > player_score:
        return "Computer wins!"
    else:
        return "It's a tie!"

result = simulate_blackjack()
print(result)

# Question 40
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

number = int(input("Enter a number to find its prime factors: "))
factors = prime_factors(number)
print(f"40. Prime factors of {number}: {factors}")
