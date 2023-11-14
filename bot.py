import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
import time
import toga

# Define patterns and responses
pairs = [
    ["hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you?", ["I'm good, thanks.", "I'm doing well."]],
    ["bye|goodbye", ["Goodbye!", "Have a great day!", "See you!"]],
    ["what is Python?", ["Python is a high-level programming language."]],
    ["how do I comment in Python?", ["You can use '#' for single-line comments."]],
    ["how do I create a function?", ["Use the 'def' keyword to define a function."]],
    ["what are lists?", ["Lists are ordered collections in Python."]],
    ["how do I loop in Python?", ["You can use 'for' and 'while' loops."]],
    ["what is a module?", ["A module is a file containing Python code."]],
    ["how do I import a module?", ["Use the 'import' keyword to import a module."]],
    ["what is indentation?", ["Indentation is used for code blocks in Python."]],
    ["how do I open a file?", ["You can use 'open()' function to open files."]],
    ["what is a dictionary?", ["A dictionary is a key-value store in Python."]],
    ["how do I install packages?", ["Use 'pip install package-name' to install packages."]],
    ["what is a variable?", ["A variable is a named storage location in memory."]],
    ["how do I assign a value to a variable?", ["You can use the '=' operator to assign a value."]],
    ["what are data types?", ["Data types define the type of value a variable can hold."]],
    ["what are integers?", ["Integers are whole numbers without decimal points."]],
    ["what are floats?", ["Floats are numbers with decimal points."]],
    ["what are strings?", ["Strings are sequences of characters."]],
    ["how do I concatenate strings?", ["You can use the '+' operator to concatenate strings."]],
    ["what is type conversion?", ["Type conversion is changing the type of a value."]],
    ["how do I take user input?", ["You can use 'input()' function to get user input."]],
    ["how do I convert a string to an integer?", ["Use 'int()' function for string-to-integer conversion."]],
    ["how do I convert a string to a float?", ["Use 'float()' function for string-to-float conversion."]],
    ["what are boolean values?", ["Boolean values are 'True' or 'False'."]],
    ["how do I use conditional statements?", ["You can use 'if', 'elif', and 'else' for conditionals."]],
    ["how do I use loops?", ["Use 'for' and 'while' loops for iteration."]],
    ["what is a function parameter?", ["A parameter is a value passed to a function."]],
    ["what is a function return value?", ["A return value is the result of a function."]],
    ["how do I define default function parameters?", ["Assign a default value in the function definition."]],
    ["what is a lambda function?", ["A lambda function is an anonymous function."]],
    ["what is a list comprehension?", ["A list comprehension is a concise way to create lists."]],
    ["what is a tuple?", ["A tuple is an immutable ordered collection."]],
    ["what is a set?", ["A set is an unordered collection of unique elements."]],
    ["what is a dictionary?", ["A dictionary is a key-value store."]],
    ["how do I add items to a list?", ["Use the 'append()' method to add items to a list."]],
    ["how do I remove items from a list?", ["Use methods like 'remove()' and 'pop()'."]],
    ["how do I access elements in a list?", ["Use index numbers to access list elements."]],
    ["how do I find the length of a list?", ["Use 'len()' function to get the length of a list."]],
    ["how do I sort a list?", ["Use the 'sort()' method for in-place sorting."]],
    ["what are modules in Python?", ["Modules are files containing Python code."]],
    ["how do I create my own module?", ["Create a '.py' file and write your functions or variables."]],
    ["what is a class?", ["A class is a blueprint for creating objects."]],
    ["how do I create a class?", ["Use the 'class' keyword and define methods and attributes."]],
    ["what is object-oriented programming (OOP)?", ["OOP is a programming paradigm based on objects."]],
    ["what is inheritance?", ["Inheritance allows a class to inherit attributes and methods from another."]],
    ["what is method overriding?", ["Method overriding is providing a new implementation for a base class method."]],
    ["how do I handle exceptions?", ["Use 'try', 'except', 'else', and 'finally' blocks."]],
    ["what is file handling?", ["File handling is reading from and writing to files."]],
    ["how do I read from a file?", ["Use 'open()' and 'read()' or 'readline()' methods."]],
    ["how do I write to a file?", ["Use 'open()' with 'write()' or 'writelines()' methods."]],
    ["what is a generator?", ["A generator is a type of iterable that generates values on-the-fly."]],
    ["how do I define a generator?", ["Use a function with 'yield' instead of 'return'."]],
    ["what is a decorator?", ["A decorator is a function that modifies the behavior of another function."]],
    ["how do I use decorators?", ["Use the '@' symbol above a function definition."]],
    ["what are comprehensions?", ["Comprehensions are concise ways to create sequences."]],
    ["what is a virtual environment?", ["A virtual environment isolates Python packages for different projects."]],
    ["how do I create a virtual environment?", ["Use 'venv' module or 'virtualenv' package."]],
    ["what is pip?", ["Pip is a package installer for Python."]],
    ["how do I install packages using pip?", ["Use 'pip install package-name'."]],
    ["how do I manage dependencies?", ["Use 'requirements.txt' to list dependencies for your project."]],
    ["what is a package?", ["A package is a collection of modules and sub-packages."]],
    ["how do I create my own package?", ["Organize your modules in a directory with '__init__.py'."]],

    
    ["how do I comment in Python?", ["You can use '#' for single-line comments."]],
    ["how do I create a function?", ["Use the 'def' keyword to define a function."]],
    ["what are lists?", ["Lists are ordered collections in Python."]],
    ["how do I loop in Python?", ["You can use 'for' and 'while' loops."]],
    ["what is a module?", ["A module is a file containing Python code."]],
    ["how do I import a module?", ["Use the 'import' keyword to import a module."]],
    ["what is indentation?", ["Indentation is used for code blocks in Python."]],
    ["how do I open a file?", ["You can use 'open()' function to open files."]],
    ["what is a dictionary?", ["A dictionary is a key-value store in Python."]],
    ["what is a variable?", ["A variable holds a value in Python."]],
    ["how do I print to the console?", ["Use 'print()' function to display output."]],
    ["what is a class?", ["A class is a blueprint for creating objects."]],
    ["how do I get user input?", ["Use 'input()' function to get user input."]],
    ["what is a tuple?", ["A tuple is an immutable collection in Python."]],
    ["how do I format strings?", ["You can use f-strings or the 'format()' method."]],
    ["what is an if statement?", ["An if statement is used for conditional execution."]],
    ["how do I calculate math in Python?", ["Use arithmetic operators like +, -, *, /."]],
    ["what is a set?", ["A set is an unordered collection of unique items."]],
    ["how do I handle exceptions?", ["Use 'try' and 'except' for error handling."]],
    ["what is inheritance?", ["Inheritance allows a class to inherit attributes from another."]],


    ["what is a loop?", ["A loop is used to repeat a block of code."]],
    ["how do I remove an item from a list?", ["Use methods like 'remove()' or 'pop()'."]],
    ["what is a lambda function?", ["A lambda function is an anonymous function."]],
    ["how do I find the length of a string?", ["Use 'len()' function for string length."]],
    ["what is the 'range()' function?", ["'range()' generates a sequence of numbers."]],
    ["how do I format date and time?", ["Use the 'datetime' module for formatting."]],
    ["what is a generator?", ["A generator produces values on the fly."]],
    ["how do I sort a list?", ["Use the 'sort()' method for sorting."]],
    ["what is a virtual environment?", ["A virtual environment isolates Python projects."]],
    ["how do I write a docstring?", ["A docstring provides documentation for functions."]],
    

    
    ["what is the difference between '==' and 'is'?", ["'==' compares values, 'is' checks identity."]],
    ["how do I convert data types?", ["Use functions like 'int()', 'str()', 'float()'."]],
    ["what is a module in Python?", ["A module is a file containing Python code."]],
    ["how do I create a virtual environment?", ["Use 'virtualenv' or 'venv' to create one."]],
    ["what is list comprehension?", ["List comprehension creates lists concisely."]],
    ["how do I find the maximum and minimum values?", ["Use 'max()' and 'min()' functions."]],
    ["what is a decorator?", ["A decorator modifies functions or methods."]],
    ["how do I work with JSON data?", ["Use 'json' module to encode and decode JSON."]],
    ["what is recursion?", ["Recursion is a function calling itself."]],
    ["how do I split a string into a list?", ["Use 'split()' method with a delimiter."]],
    ["what is a generator expression?", ["A generator expression creates an iterator."]],
    ["how do I work with files and directories?", ["Use 'os' and 'shutil' modules for file operations."]],
    ["what is a private variable?", ["A private variable starts with an underscore."]],
    ["how do I remove duplicates from a list?", ["Convert to a 'set' and back to a 'list'."]],
    ["what is the 'map()' function?", ["'map()' applies a function to elements."]],
    ["how do I find the index of an item in a list?", ["Use 'index()' method."]],
    ["what is the 'zip()' function?", ["'zip()' combines multiple iterables."]],
    ["how do I handle time delays?", ["Use the 'time' module for delays."]],
    ["what is the 'with' statement?", ["'with' manages resources like files."]],
    ["how do I raise an exception?", ["Use 'raise' statement to raise exceptions."]],
    


    ["how do I reverse a list?", ["Use 'reverse()' method or slicing."]],
    ["what is a package in Python?", ["A package is a collection of modules."]],
    ["how do I concatenate strings?", ["Use the '+' operator or 'join()' method."]],
    ["what is a docstring?", ["A docstring is a multi-line comment for documentation."]],
    ["how do I handle keyboard interrupts?", ["Use 'KeyboardInterrupt' exception."]],
    ["what is a list slice?", ["A slice extracts a portion of a list."]],
    ["how do I check if a key exists in a dictionary?", ["Use the 'in' keyword."]],
    ["what is a method?", ["A method is a function defined inside a class."]],
    ["how do I clone a list?", ["Use list slicing or the 'copy()' method."]],
    ["what is polymorphism?", ["Polymorphism allows objects to take on multiple forms."]],
    ["how do I format numbers?", ["Use the 'format()' function."]],
    ["what is the 'random' module?", ["'random' generates random numbers."]],
    ["how do I convert a string to lowercase?", ["Use the 'lower()' method."]],
    ["what is a constructor?", ["A constructor initializes object attributes."]],
    ["how do I find the absolute value?", ["Use the 'abs()' function."]],
    ["what is an else statement?", ["An else statement follows an if statement."]],
    ["how do I copy files?", ["Use 'shutil.copy()' for file copying."]],
    ["what is the 'enumerate()' function?", ["'enumerate()' adds an index to an iterable."]],
    ["how do I check the type of an object?", ["Use the 'type()' function."]],
    ["what is a boolean?", ["A boolean is a data type with values 'True' or 'False'."]],
    ["how do I raise a custom exception?", ["Define a class inheriting from 'Exception'."]],
    ["what is a matrix?", ["A matrix is a 2D array-like structure."]],
    ["how do I use the 'time' module?", ["'time' provides time-related functions."]],
    ["what is the 'filter()' function?", ["'filter()' selects elements based on a function."]],
    ["how do I find the most common element in a list?", ["Use 'collections.Counter'."]],
    ["what is a recursive function?", ["A recursive function calls itself."]],
    ["how do I check if a file exists?", ["Use 'os.path.exists()'."]],
    ["what is the 'format()' method?", ["'format()' replaces placeholders in strings."]],
    ["how do I find the power of a number?", ["Use the '**' operator or 'math.pow()'."]],
    ["what is a dictionary comprehension?", ["Dictionary comprehension creates dictionaries."]],
    ["how do I work with command line arguments?", ["Use the 'sys.argv' list from the 'sys' module."]],
    


    ["what is the 'itertools' module?", ["'itertools' provides tools for iterators and loops."]],
    ["how do I find the factorial of a number?", ["Use a loop or 'math.factorial()'."]],
    ["what is a lambda function?", ["A lambda function is an anonymous function."]],
    ["how do I reverse a string?", ["Use string slicing with a step of -1."]],
    ["what is a shallow copy?", ["A shallow copy copies outer objects, but not nested ones."]],
    ["how do I iterate over multiple lists?", ["Use 'zip()' to iterate over multiple iterables."]],
    ["what is a context manager?", ["A context manager manages resources with 'with' statement."]],
    ["how do I use regular expressions?", ["Use the 're' module for pattern matching."]],
    ["what is a metaclass?", ["A metaclass defines the behavior of a class."]],
    ["how do I remove whitespace from a string?", ["Use 'strip()' to remove leading/trailing spaces."]],



    ["how do I find the sum of elements in a list?", ["Use the 'sum()' function."]],
    ["what is the 'classmethod' decorator?", ["'classmethod' defines a method on a class."]],
    ["how do I split a string into characters?", ["Strings are already iterable as characters."]],
    ["what is a list comprehension?", ["List comprehension creates lists concisely."]],
    ["how do I find the square root?", ["Use the '**' operator or 'math.sqrt()'."]],
    ["what is a keyword argument?", ["A keyword argument is passed by its name."]],
    ["how do I remove leading/trailing characters from a string?", ["Use 'strip()', 'lstrip()', 'rstrip()'."]],
    ["what is the 'self' parameter?", ["The 'self' parameter refers to the instance of a class."]],
    ["how do I create a range of numbers?", ["Use 'range()' function with start, stop, and step."]],
    ["what is a module alias?", ["A module alias is a short name for a module."]],
    ["how do I convert a list to a string?", ["Use 'join()' method with an empty separator."]],
    ["what is the 'map()' function?", ["'map()' applies a function to elements of an iterable."]],
    ["how do I find the length of a list?", ["Use the 'len()' function."]],
    ["what is the 'locals()' function?", ["'locals()' returns a dictionary of the current namespace."]],
    ["how do I capitalize the first letter of a string?", ["Use 'capitalize()' method or 'title()' method."]],
    ["what is the 'assert' statement?", ["'assert' tests if a condition is true."]],
    ["how do I open a CSV file?", ["Use the 'csv' module to read/write CSV files."]],
    ["what is the 'try...except' block?", ["'try' handles exceptions and 'except' defines handlers."]],
    ["how do I convert a string to uppercase?", ["Use 'upper()' method."]],
    ["what is the 'any()' function?", ["'any()' returns 'True' if at least one element is true."]],
    


    ["generate a Fibonacci sequence of length 10", ["def fibonacci(n):\n    fib_sequence = [0, 1]\n    while len(fib_sequence) < n:\n        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])\n    return fib_sequence\nfibonacci_sequence = fibonacci(10)"]],
    ["create a dictionary comprehension", ["numbers = [1, 2, 3, 4, 5]\nsquare_dict = {num: num ** 2 for num in numbers}"]],
    ["generate a list of prime numbers up to 50", ["def is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, int(num ** 0.5) + 1):\n        if num % i == 0:\n            return False\n    return True\nprime_numbers = [x for x in range(2, 51) if is_prime(x)]"]],
    ["create a class with methods", ["class Calculator:\n    def __init__(self):\n        self.value = 0\n    def add(self, num):\n        self.value += num\n    def get_value(self):\n        return self.value\nmy_calculator = Calculator()\nmy_calculator.add(5)\nresult = my_calculator.get_value()"]],
    ["generate a list of strings with lengths", ["word_list = ['apple', 'banana', 'cherry', 'date']\nlength_list = [len(word) for word in word_list]"]],
    ["how do I sort a list of dictionaries by a key?", ["sorted_list = sorted(dictionary_list, key=lambda x: x['key'])"]],
    ["create a function that returns the factorial of a number", ["def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)"]],
    ["generate a list of unique elements from a list", ["unique_list = list(set(original_list))"]],
    ["how do I concatenate two strings?", ["concatenated_string = string1 + string2"]],
    ["create a nested loop to generate a multiplication table", ["for i in range(1, 11):\n    for j in range(1, 11):\n        print(i * j, end='\\t')\n    print()"]],
    



    ["generate a random number between 1 and 10", ["import random\nrandom_number = random.randint(1, 10)"]],
    ["create a simple for loop", ["for i in range(5):\n    print(i)"]],
    ["generate a list of even numbers from 1 to 10", ["even_numbers = [x for x in range(1, 11) if x % 2 == 0]"]],
    ["how do I read a file in Python?", ["with open('filename.txt', 'r') as file:\n    content = file.read()"]],
    ["generate a dictionary with keys and values", ["my_dict = {'key1': 'value1', 'key2': 'value2'}"]],
    ["create a function that adds two numbers", ["def add_numbers(a, b):\n    return a + b"]],
    ["generate a list of squares from 1 to 5", ["squares = [x ** 2 for x in range(1, 6)]"]],
    ["how do I write to a file in Python?", ["with open('output.txt', 'w') as file:\n    file.write('Hello, World!')"]],
    ["create a while loop that counts from 1 to 5", ["count = 1\nwhile count <= 5:\n    print(count)\n    count += 1"]],
    ["generate a list of uppercase strings from a list", ["uppercase_strings = [s.upper() for s in string_list]"]],
  

    ["create a class for managing a bank account", ["class BankAccount:\n    def __init__(self, account_number, balance=0):\n        self.account_number = account_number\n        self.balance = balance\n    def deposit(self, amount):\n        self.balance += amount\n    def withdraw(self, amount):\n        if amount <= self.balance:\n            self.balance -= amount\n        else:\n            print('Insufficient balance')\n    def get_balance(self):\n        return self.balance\nmy_account = BankAccount('123456')"]],
    ["generate code to read data from a CSV file and calculate statistics", ["import csv\nwith open('data.csv', 'r') as file:\n    csv_reader = csv.reader(file)\n    data = [row for row in csv_reader]\nnumeric_column = [float(row[2]) for row in data]\naverage = sum(numeric_column) / len(numeric_column)\nmaximum = max(numeric_column)\nminimum = min(numeric_column)"]],
    ["create a web scraping script using 'requests' and 'beautifulsoup'", ["import requests\nfrom bs4 import BeautifulSoup\nurl = 'https://example.com'\nresponse = requests.get(url)\nsoup = BeautifulSoup(response.text, 'html.parser')\nlinks = soup.find_all('a')\nfor link in links:\n    print(link['href'])"]],
    ["generate a basic Flask web application", ["from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run()"]],
    ["create a function to check if a string is a palindrome", ["def is_palindrome(string):\n    clean_string = string.lower().replace(' ', '')\n    return clean_string == clean_string[::-1]"]],
    ["generate code to parse JSON data and perform operations", ["import json\nwith open('data.json', 'r') as file:\n    json_data = json.load(file)\nusers = json_data['users']\ntotal_age = sum(user['age'] for user in users)\naverage_age = total_age / len(users)"]],
    ["create a program that simulates a basic ATM machine", ["class ATM:\n    def __init__(self, balance=0):\n        self.balance = balance\n    def deposit(self, amount):\n        self.balance += amount\n    def withdraw(self, amount):\n        if amount <= self.balance:\n            self.balance -= amount\n        else:\n            print('Insufficient balance')\n    def check_balance(self):\n        return self.balance\nmy_atm = ATM(1000)"]],
    ["generate code to perform matrix multiplication", ["import numpy as np\nmatrix1 = np.array([[1, 2], [3, 4]])\nmatrix2 = np.array([[5, 6], [7, 8]])\nresult = np.dot(matrix1, matrix2)"]],
    ["create a function that calculates the greatest common divisor (GCD)", ["def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a"]],
    ["generate code to sort a list of dictionaries by multiple keys", ["sorted_list = sorted(dictionary_list, key=lambda x: (x['key1'], x['key2']))"]],
    

    ["create a function to find the factorial of a number using recursion", ["def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)"]],
    ["generate code to implement a binary search algorithm", ["def binary_search(arr, target):\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1"]],
    ["create a program to simulate a basic quiz game", ["class QuizGame:\n    def __init__(self, questions):\n        self.questions = questions\n        self.score = 0\n    def play_quiz(self):\n        for question, answer in self.questions.items():\n            user_answer = input(question)\n            if user_answer.lower() == answer.lower():\n                self.score += 1\n        print(f'Your score: {self.score}')\nquestions = {\n    'What is the capital of France?': 'Paris',\n    'What is 2 + 2?': '4'\n}\nmy_quiz = QuizGame(questions)\nmy_quiz.play_quiz()"]],
    ["generate code to implement selection sort for a list", ["def selection_sort(arr):\n    for i in range(len(arr) - 1):\n        min_index = i\n        for j in range(i + 1, len(arr)):\n            if arr[j] < arr[min_index]:\n                min_index = j\n        arr[i], arr[min_index] = arr[min_index], arr[i]"]],
    ["create a program that generates a multiplication table as a text file", ["with open('multiplication_table.txt', 'w') as file:\n    for i in range(1, 11):\n        for j in range(1, 11):\n            file.write(f'{i} x {j} = {i*j}\\n')"]],
    ["generate code to implement a stack data structure", ["class Stack:\n    def __init__(self):\n        self.items = []\n    def push(self, item):\n        self.items.append(item)\n    def pop(self):\n        if not self.is_empty():\n            return self.items.pop()\n    def is_empty(self):\n        return len(self.items) == 0"]],
    ["create a program to read data from an API using the 'requests' library", ["import requests\nresponse = requests.get('https://api.example.com/data')\ndata = response.json()"]],
    ["generate code to perform matrix addition and subtraction", ["import numpy as np\nmatrix1 = np.array([[1, 2], [3, 4]])\nmatrix2 = np.array([[5, 6], [7, 8]])\naddition_result = matrix1 + matrix2\nsubtraction_result = matrix1 - matrix2"]],
    ["create a program that calculates compound interest", ["def calculate_interest(principal, rate, time):\n    compound_interest = principal * (1 + rate/100) ** time - principal\n    return compound_interest"]],
    ["generate code to implement the insertion sort algorithm", ["def insertion_sort(arr):\n    for i in range(1, len(arr)):\n        key = arr[i]\n        j = i - 1\n        while j >= 0 and key < arr[j]:\n            arr[j + 1] = arr[j]\n            j -= 1\n        arr[j + 1] = key"]],
    


    ["create a function to check if a number is prime", ["def is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, int(num ** 0.5) + 1):\n        if num % i == 0:\n            return False\n    return True"]],
    ["generate code to implement a bubble sort algorithm", ["def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]"]],
    ["create a program to reverse a string", ["def reverse_string(s):\n    return s[::-1]"]],
    ["generate code to calculate the area of a triangle", ["def triangle_area(base, height):\n    return 0.5 * base * height"]],
    ["create a function to calculate the factorial of a number using iteration", ["def factorial_iterative(n):\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result"]],
    ["generate code to find the largest element in a list", ["def find_largest_element(arr):\n    largest = arr[0]\n    for num in arr:\n        if num > largest:\n            largest = num\n    return largest"]],
    ["create a program to convert temperatures between Celsius and Fahrenheit", ["def celsius_to_fahrenheit(celsius):\n    return (celsius * 9/5) + 32\n\ndef fahrenheit_to_celsius(fahrenheit):\n    return (fahrenheit - 32) * 5/9"]],
    ["generate code to calculate the sum of digits in a number", ["def sum_of_digits(number):\n    total = 0\n    while number > 0:\n        total += number % 10\n        number //= 10\n    return total"]],
    ["create a program to check if a string is a palindrome", ["def is_palindrome(s):\n    s = s.lower().replace(' ', '')\n    return s == s[::-1]"]],
    ["generate code to reverse words in a sentence", ["def reverse_words(sentence):\n    words = sentence.split()\n    reversed_sentence = ' '.join(words[::-1])"]],
    ["create a function to calculate the power of a number", ["def power(base, exponent):\n    return base ** exponent"]],
    ["generate code to calculate the greatest common divisor (GCD) using Euclidean algorithm", ["def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a"]],
    ["create a program to find the least common multiple (LCM) of two numbers", ["def lcm(a, b):\n    return (a * b) // gcd(a, b)"]],
    ["generate code to reverse a linked list", ["class Node:\n    def __init__(self, value):\n        self.value = value\n        self.next = None\n\ndef reverse_linked_list(head):\n    prev = None\n    current = head\n    while current:\n        next_node = current.next\n        current.next = prev\n        prev = current\n        current = next_node\n    return prev"]],
    ["create a function to find the median of a list of numbers", ["def find_median(numbers):\n    numbers.sort()\n    n = len(numbers)\n    if n % 2 == 1:\n        return numbers[n // 2]\n    else:\n        return (numbers[n // 2 - 1] + numbers[n // 2]) / 2"]],
    ["generate code to implement a linear search algorithm", ["def linear_search(arr, target):\n    for i in range(len(arr)):\n        if arr[i] == target:\n            return i\n    return -1"]],
    ["create a program to calculate the factorial of a number using memoization", ["factorial_memo = {}\n\ndef factorial_memoization(n):\n    if n in factorial_memo:\n        return factorial_memo[n]\n    if n == 0:\n        return 1\n    result = n * factorial_memoization(n - 1)\n    factorial_memo[n] = result\n    return result"]],
    ["generate code to calculate the average of numbers in a list", ["def calculate_average(numbers):\n    return sum(numbers) / len(numbers)"]],
    ["create a function to find the intersection of two lists", ["def list_intersection(list1, list2):\n    return list(set(list1) & set(list2))"]],
    ["generate code to implement a binary search tree", ["class TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BinarySearchTree:\n    def __init__(self):\n        self.root = None\n    def insert(self, value):\n        if not self.root:\n            self.root = TreeNode(value)\n        else:\n            self._insert_recursive(self.root, value)\n    def _insert_recursive(self, node, value):\n        if value < node.value:\n            if node.left is None:\n                node.left = TreeNode(value)\n            else:\n                self._insert_recursive(node.left, value)\n        else:\n            if node.right is None:\n                node.right = TreeNode(value)\n            else:\n                self._insert_recursive(node.right, value)"]],
    ["create a program to find the longest common subsequence of two strings", ["def longest_common_subsequence(s1, s2):\n    m, n = len(s1), len(s2)\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if s1[i - 1] == s2[j - 1]:\n                dp[i][j] = dp[i - 1][j - 1] + 1\n            else:\n                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])\n    lcs = ''\n    i, j = m, n\n    while i > 0 and j > 0:\n        if s1[i - 1] == s2[j - 1]:\n            lcs = s1[i - 1] + lcs\n            i -= 1\n            j -= 1\n        elif dp[i - 1][j] > dp[i][j - 1]:\n            i -= 1\n        else:\n            j -= 1\n    return lcs"]],
    ["generate code to implement a hash table using chaining for collision resolution", ["class HashTable:\n    def __init__(self, size):\n        self.size = size\n        self.table = [[] for _ in range(size)]\n    def _hash(self, key):\n        return sum(ord(char) for char in key) % self.size\n    def insert(self, key, value):\n        index = self._hash(key)\n        self.table[index].append((key, value))\n    def get(self, key):\n        index = self._hash(key)\n        for k, v in self.table[index]:\n            if k == key:\n                return v\n        return None"]],
    ["create a program to implement a basic queue data structure", ["class Queue:\n    def __init__(self):\n        self.items = []\n    def enqueue(self, item):\n        self.items.insert(0, item)\n    def dequeue(self):\n        if not self.is_empty():\n            return self.items.pop()\n    def is_empty(self):\n        return len(self.items) == 0"]],
    ["generate code to implement the Sieve of Eratosthenes algorithm for prime numbers", ["def sieve_of_eratosthenes(limit):\n    primes = [True] * (limit + 1)\n    primes[0] = primes[1] = False\n    for i in range(2, int(limit ** 0.5) + 1):\n        if primes[i]:\n            for j in range(i * i, limit + 1, i):\n                primes[j] = False\n    prime_numbers = [i for i, is_prime in enumerate(primes) if is_prime]\n    return prime_numbers"]],
    ["create a program to implement a basic stack using linked list", ["class Node:\n    def __init__(self, value):\n        self.value = value\n        self.next = None\n\nclass Stack:\n    def __init__(self):\n        self.top = None\n    def push(self, item):\n        new_node = Node(item)\n        new_node.next = self.top\n        self.top = new_node\n    def pop(self):\n        if not self.is_empty():\n            popped_item = self.top.value\n            self.top = self.top.next\n            return popped_item\n    def is_empty(self):\n        return self.top is None"]],
    ["generate code to calculate the factorial of a number using memoization", ["factorial_memo = {}\n\ndef factorial_memoization(n):\n    if n in factorial_memo:\n        return factorial_memo[n]\n    if n == 0:\n        return 1\n    result = n * factorial_memoization(n - 1)\n    factorial_memo[n] = result\n    return result"]],
    ["create a program to implement a simple interpreter for arithmetic expressions", ["def evaluate_expression(expression):\n    try:\n        return eval(expression)\n    except:\n        return 'Invalid expression'"]],
    






]

chatbot = Chat(pairs, reflections)



# Function to handle user input
def send_message():
    user_input = user_input_field.get()
    if user_input.lower() == 'bye':
        response_text.insert(tk.END, "ChatBot: Goodbye!\n")
        root.quit()
    response_text.insert(tk.END, "You: " + user_input + "\n")
    user_input_field.delete(0, tk.END)

    response = chatbot.respond(user_input)
    if response == "I'm sorry, I don't have an answer for that at the moment.":
        response_text.insert(tk.END, "ChatBot: " + response + "\n", "gold")
    else:
        response_text.insert(tk.END, "ChatBot: " + response + "\n")
    response_text.update()  # Update the text widget
    simulate_typing(response + "\n")

# ... (rest of the code remains the same)


# Function to simulate typing effect
def simulate_typing(response):
    for char in response:
        response_text.insert(tk.END, char)
        response_text.update()  # Update the text widget
        time.sleep(0.05)  # Adjust the typing speed
 
# Create the main window
root = tk.Tk() 
root.title("ChatBot")
root.geometry("600x900")

# Customize colors
root.configure(bg="#333333")  # Set the background color of the main window

# Initializing animation
initializing_label = tk.Label(root, text="Initializing...", fg="#FFD700", bg="#333333", font=("Helvetica", 16))
initializing_label.pack(pady=100)
root.update()

dots = ""
for _ in range(10):  # Simulate initialization time with 3 dots
    dots += "."
    initializing_label.config(text="Initializing" + dots)
    root.update()
    time.sleep(0.1)

initializing_label.destroy()  # Remove the initializing label

response_text = scrolledtext.ScrolledText(root, width=80, height=40, bg="#222222", fg="#32CD32", insertbackground="#32CD32")
response_text.tag_configure("gold", foreground="#FFD700")  # Define a custom tag for gold text

response_text.pack(padx=10, pady=10)

user_input_field = tk.Entry(root, width=40, bg="#333333", fg="white", insertbackground="white")
user_input_field.pack(padx=10, pady=10)
user_input_field.bind("<Return>", lambda event: send_message())  # Bind Enter key event

send_button = tk.Button(root, text="Send", command=send_message, bg="#FFD700", fg="#333333")
send_button.pack()

# Start the GUI event loop
root.mainloop()
