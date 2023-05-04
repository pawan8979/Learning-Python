"""
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword 
syntax:
lambda arguments: expression

Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
"""

# Normal Function:
def double(x):
  return x * 2

# Lambda function:
double= lambda x: x * 2
print(double(5))


# Lambda function with Multiple Arguments
# Normal function:
def multiply(x, y):
    return x * y
# Lambda function:
lambda x, y: x * y

# Lambda functions can also include multiple statements, but they are limited to a single expression.
lambda x, y: print(f'{x} * {y} = {x * y}')

# Passing lambda function as argument to another function
cube= lambda x: x*x*x
def appl(fx, value):
   return 6+ fx(value) #6+cube(2)
print(appl(cube,2))
print(appl(lambda x: x*x, 2)) #fx= x*x

# Note: Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce.