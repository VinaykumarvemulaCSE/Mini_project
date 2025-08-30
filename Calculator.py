""" calculator with 2 numbers and 7 arthimetic operator
By python code"""
choice = input("Do you want to calculate (Yes/No): ")
while choice=="Yes":
 num1 = float(input("Enter your First Number : "))
 num2 = float(input("Enter your Second Number: "))
 print("NOTE : Choose only Arithmetic Operators")
 print("For Ex:- \n(+) for addition ,(-) for subtraction ")
 print("(*) for multiplication ,(/) for division")
 print("(//)for floor division,(%) for module,(**)for exponential")
 Operator = input("Enter your Operator: ")
 if Operator == "+" :
     print(f"Addition of 2 numbers is :{num1+num2}")
 elif Operator == "-" :
     print(f"Subtraction of 2 numbers is:{num1-num2}")
 elif Operator == "*" :
     print(f"Multiplication of 2 numbers is:{num1*num2}")
 elif Operator == "/" :
   if num2!=0 :
     print(f"Division of 2 numbers is:{num1/num2}")
   else :
     print("Error!!!: Division by zero is not allowed")
 elif Operator == "//" :
   if num2!=0 :
     print(f"Floor Division of 2 numbers is:{num1//num2}")
   else :
     print("Error!!!: Division by zero is not allowed")
 elif Operator == "%" :
   if num2!=0 :
     print(f"Module of 2 numbers is:{num1%num2}")
   else :
     print("Error!!!: Division by zero is not allowed")
 elif Operator == "**" :
   print(f" {num1} to the power of {num2} is:{num1**num2}")
 else :
   print("You have Entered wrong operator!!!")
 Choice=input("\n \n Do you want to calculate again(Yes/No):")
 if Choice=="Yes":
   continue
 else :
  break
print("Thankyou for using our calculator")
# Successfully completed calculator