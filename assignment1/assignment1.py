# Write your code here.
import logging

logging.basicConfig(level=logging.DEBUG)

"""def multiply(a, b):
    logging.debug(f"Multiplying {a} and {b}")
    result = a * b
    logging.info(f"Result is: {result}")
    return result
"""

#Task 1
def hello():
    greet = "Hello!"
    return greet

hello()

#Task 2
def greet(name):
    greet = f"Hello, {name}!"
    return greet

greet("Valeri")

#Task 3 for my notes 
def calc(num1, num2, operator = "multiply"):
    try:
        if(operator == "multiply"):
            return num1 * num2
        elif(operator == "add"):
            return num1 + num2
        elif(operator == "subtract"):
            return num1 - num2
        elif(operator == "divide"):
                return num1 / num2
        elif(operator == "modulo"):
            return num1 % num2
        elif(operator == "int_divide"):
            return num1 // num2
        elif(operator == "power"):
            result = num1 ** num2
            return result
    except ZeroDivisionError:
        return  "You can't divide by 0!" 
    except TypeError:  
         return "You can't multiply those values!"
        
calc(5, 6, "add")

# Task 3 for my notes
def calc(num1, num2, operator = "multiply"):
    try:
        match operator:
            case "multiply":
                return num1 * num2
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2                
    except ZeroDivisionError: 
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
        
calc(5, 6, "divide")
    
# Task 4
def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)            
            case "int":
                return int(value)        
    except ValueError: 
        return f"You can't convert {value} into a {type}."
    
data_type_conversion("110", "int")

data_type_conversion("5.5", "float")

data_type_conversion(7, "float")

data_type_conversion(91.1, "str")

data_type_conversion("banana", "int")

# Task 5

def grade(*args):
    try:
        average = sum(args) / len(args) 
        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        elif average >= 50:
            grade = "F"
        return grade 
    except TypeError: 
        return "Invalid data was provided."
    
#print(grade(75, 85, 95 ))
grade("three", "blind", "mice")

# Task 6
def repeat(greeting, count):
    result = ""
    for _ in range(count):      
        result += greeting
    return result
repeat("hey ", 4)

#Task 7 
def student_scores(score, **kwargs):
    print("Students scores: ")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    best_score = -float('inf')
    best_student = ""
    for key, value in kwargs.items():
        if int(value) > best_score:
            best_score = value
            best_student = key
    try:
        match score: 
            case "best":
                return best_student
            case "mean":
                return sum(kwargs.values())/ len(kwargs.values())
    except TypeError:
        return "Invalid Data"
    
student_scores("mean", Alice=95, Tom=99, Jake=88)

#Task 8 for my notes
def titleize(title):
    new_title = title.split()
    new_title[0] = new_title[0].capitalize()
    new_title[2] = new_title[2].capitalize()
    joining_title = " ".join(new_title)
    return joining_title

print(titleize("war and peace"))

#Task 8
def titleize(title):
    words = title.split()
    small_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    for i, word in enumerate(words): #enumerate gives index + value at the same time
        if i == 0 or i == len(words) - 1 or word not in small_words:
            words[i] = word.capitalize()
    return " ".join(words)

print(titleize("war and peace"))
print(titleize("a separate peace"))
print(titleize("after on"))

#Task 9 
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"        
    return result 

print(hangman("albaphet", "abcd"))

#Task 10 
def pig_latin(sentence):
    try:
        vowels = "aeiou"
        add_key_word = "ay"
        pig_latin_words = []
        result = ""
        for word in sentence.lower().split():
            if word[0] in vowels:
                result = word + add_key_word 
                pig_latin_words.append(result)
                continue
            else:
                for i, letter in enumerate(word):
                    if letter in vowels:
                        if letter == "u" and i > 0 and word[i-1] == "q":
                            continue
                        result = word[i:] + word[:i] + add_key_word
                        pig_latin_words.append(result)
                        break
        return " ".join(pig_latin_words)
    except TypeError:
        return "Can't return the result."

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))