# 1. Write a program that takes an integer input from the user and checks whether the number is odd or even

print("even or odd number cheaker")
num=int(input("ENTER THE NUMBER WHICH YOU WANT TO CHECK : "))
if (num% 2==0):
  print(f"{num} is even ")
else :
  print(f"{num} is odd ")

# 2. Write a program that takes three numbers as input and prints the largest of the three.
a=int(input(" enter the value of a : "))
b=int(input(" enter the value of b : "))
c=int(input(" enter the value of c : "))
if (a>b and a>c):
  print(f"{a} is largest number")
elif(b>a and b>c):
    print(f"{b} is largest number")
else:
  print(f"{c} is largest number")

# 3. Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
year=int(input("ENTER THE YEAR : "))
if (year%4==0) and (year!=100 or year%400==0 ):
  print(f"{year} IS A LEAP YEAR ")
else:
  print(f"{year} IS A NOT LEAP YEAR ")

''' Q4. Write a program that takes a percentage (integer) as input and prints the corresponding grade based on the following criteria:
   >= 90: Grade A
   >= 80: Grade B
   >= 70: Grade C
   >= 60: Grade D
   < 60: Grade F
'''
PERCENTAGE = int(input(" enter the percentage of marks : "))
if (PERCENTAGE >=90):
  print("GRADE A")
elif(PERCENTAGE>=80):
  print("GRADE B")
elif(PERCENTAGE>=70):
  print("GRADE C")
elif(PERCENTAGE>=60):
  print("GRADE D")
elif(PERCENTAGE<60):
  print("GRADE F")
else:
  print ("INVALID INPUT!!")

# 5. Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.
LETTER = input("ENTER THE LETTER TO CHECK VOWEL OR CONSONANT : ").lower()
if LETTER in 'aeiou':
  print (f"{LETTER} is vowel")
else:
  print (f"{LETTER} is consonant")

# Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and
# performs the specified operation. Print the result based on the operation.
x=int(input("ENTER THE FIRST NUMBER : "))
y=int(input("ENTER THE SECOND NUMBER : "))
choice1=int(input("CHOOSE THE OPERATION : "))
print("1. ADDITION")
print("2. SUBSTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

if (choice1==1):
  print("ADDITION = ",x+y)
elif(choice1==2):
  print("SUBSTRACTION = ",x-y)
elif(choice1==3):
  print("MULTIPLICATION = ",x*y)
elif(choice1==4):
  print("DIVISION = ",x/y)
else:
  print("INVALID INPUT!!")

# Q7. Write a program that takes a number as input and checks whether it is positive, negative, or zero.
num1=int(input("ENTER THE NUMBER : "))
if (num1==0):
  print("it is zero")
elif (num1>0):
  print("it is positive")
if (num1<0):
  print("it is negative")

# Q8. Write a program that checks if a username and password entered by the user match the pre-set values
# username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
# "Login Failed"
username=input("ENTER THE FIRST NUMBER : ")
password=int(input("ENTER THE SECOND NUMBER : "))
if (username=="admin"):
  if (password==1234):
    print("LOGIN SUCCESSFULL!!")
  else:
    print("password wrong!!")
else:
  print("username wrong!")

# Q 9. Write a program that takes three sides of a triangle as input and checks if those sides form a valid
# triangle. A triangle is valid if the sum of any two sides is greater than the third side.
# Check conditions like a + b > c, b + c > a, and a + c > b
side1=int(input("ENTER THE FIRST SIDE : "))
side2=int(input("ENTER THE SECOND SIDE : "))
side3=int(input("ENTER THE SECOND SIDE : "))

if((side1 + side2 > side3) or (side2 + side3 > side1) or (side3 + side1 > side2) ):
  print("TRIANGLE IS POSSIBLE!!")
else:
  print("TRIANGLE IS NOT POSSIBLE!!") 

# Q11. Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount
discount=0
price=int(input("ENTER THE FIRST SIDE : "))
if(price> 1000):
  discount=price-(price*0.1)
  print(f"price after DISCOUNT : {discount}")
elif(price>500):
  discount=price-(price*0.02)
  print(f"price after DISCOUNT : {discount}")
else :
  print(f"price after DISCOUNT : {price}")

# Q 12. Write a program that takes the name of a month as input and prints the number of days in that month. Consider leap years for February.
month = input("Enter the name of a month: ").lower()
year = int(input("Enter a year: "))

if month == "january" or month == "march" or month == "july" or month == "august" or month == "october" or month == "december":
    print("31 days")
elif month == "february":
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("February has 29 days.")
    else:
        print("February has 28 days.")
elif month == "april" or month == "june" or month == "september" or month == "november":
    print("30 days")
else:
    print("Invalid month name.")

# Q 13. Write a program that simulates a simple ATM. The user should be able to:
# Check balance
# Deposit money
# Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices
