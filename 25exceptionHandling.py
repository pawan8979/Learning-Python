"""
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. 
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

Syntax:
try:
     statements which could generate 
     exception
except:
     Solution of generated exception
"""

try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

# Here is simple syntax of try....except...else blocks −

"""
try:
   You do your operations here;
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
"""

try:
    num= int(input("Enter an integer: "))
    a= [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")
else:
   print (" I am else statement")

