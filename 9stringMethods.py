a= "pawan!!"
b= "ne gi"
c= "copy!! copy  copy"
print(len(a))
print(a.upper()) #UPPER
print((a.upper()).lower()) #LOWER
print(a.rstrip("!")) #only remove tailing 
print(a.replace("pawan", "Vivek"))
print(b.split(" "))
heading= "intro tO pRoGramming"
print(heading.capitalize())

str1= "Welcome to vscode"
str2= "Welcometovscode"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(c.count("copy"))
print(c.endswith("cop"))

print(str1.endswith("to", 4, 10))
print(str1.find("to"))
print(str1.find("snake"))
print(str2.isalnum()) #space not allowed
print(str1.isalpha()) #false

str3= "we will\n"
print(str3.isprintable()) #false bcz \n

str4= "Pawan Negi"
print(str4.isspace()) #false

print(str4.swapcase())
