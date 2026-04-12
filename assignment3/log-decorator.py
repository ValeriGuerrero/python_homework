import logging

#Task 1
logging.basicConfig(filename='./decorator.log', level=logging.INFO)

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Function called: {func.__name__}")
        logging.info(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Returned: {result}")
        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello World!")

hello_world()

@logger_decorator
def num(*args):
    return True

print(num(5, 4))

@logger_decorator
def no_arguments(**kwargs):
    return logger_decorator

print(no_arguments(x=0, y=1))

