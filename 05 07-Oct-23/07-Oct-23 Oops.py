# Problem 1: Bank Account
class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")

# Problem 2: Employee Management
class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_percentage):
        return (bonus_percentage / 100) * self.salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

# Problem 3: Vehicle Rental
class VehicleRental:
    def __init__(self):
        self.available_vehicles = []

    def rent_vehicle(self, vehicle):
        if vehicle in self.available_vehicles:
            self.available_vehicles.remove(vehicle)
            print(f"{vehicle} rented successfully!")
        else:
            print(f"{vehicle} is not available for rent.")

    def return_vehicle(self, vehicle):
        self.available_vehicles.append(vehicle)
        print(f"{vehicle} returned successfully!")

    def display_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.available_vehicles:
            print(vehicle)

# Problem 4: Library Catalog
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def bookdetails(self):
        print(f"i am reading {self.title} by {self.author}")

class Library(Book):
    def __init__(self,book_id, title, author):
        super().__init__(book_id, title, author)
        self.available_books = []

    def add_book(self, book):
        self.available_books.append(book)

    def borrow_book(self, book_id):
        for book in self.available_books:
            if book.book_id == book_id:
                self.available_books.remove(book)
                print(f"{book.title} borrowed successfully!")
                return
        print("Book not found in the library.")

    def display_available_books(self):
        print("Available Books:")
        for book in self.available_books:
            print(f"{book.title} by {book.author}")

# Problem 5: Product Inventory
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_quantity(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity = new_quantity
                print(f"Quantity of {product.name} updated to {new_quantity}.")
                return
        print("Product not found in the inventory.")

    def display_available_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product.name} - Price: ${product.price} - Quantity: {product.quantity}")

# Problem 6: Shape Calculation
class Shape:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def calculate_area(self):
        import math
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Problem 7: Student Management
class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Average Grade: {self.calculate_average_grade()}")

# Problem 8: Email Management
class Email:
    def __init__(self, sender, recipient, subject, content):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.content = content

    def send_email(self):
        print(f"Email sent to {self.recipient} with subject: {self.subject}")

    def display_details(self):
        print(f"From: {self.sender}")
        print(f"To: {self.recipient}")
        print(f"Subject: {self.subject}")
        print(f"Content: {self.content}")

# Problem 9: Social Media Profile
class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_posts(self):
        print(f"Posts by {self.username}:")
        for post in self.posts:
            print(post)

    def search_posts(self, keyword):
        print(f"Posts by {self.username} containing '{keyword}':")
        for post in self.posts:
            if keyword in post:
                print(post)

# Problem 10: ToDo List
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_as_completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found in the list.")

    def display_pending_tasks(self):
        print("Pending Tasks:")
        for task in self.tasks:
            print(task)

a=Library(1,"DSA","author of DSA")
a.bookdetails()