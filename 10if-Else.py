# if-elif-else
a= int(input("Enter the age:"))
if(a>18):
        print("you can drive")
elif(a==18):
        print("you just hit maturity")
else:
        print("you cannot drive")

#nested if

num=18
if(num<0):
        print("Number is negative")

elif(num>0):
        if(num<=10):
                print("Number is btwn 1-10")
        elif(num>10 and num<=20):
                print("Number is btwn 11-20")
        else:
                print("Number is greater than 20")
else:
        print("Number is zero")