a=int(input("enter a number:"))
b=int(input("enter secomd number:"))

if a==b:
  add=a+b
  print("the sum of two number is ", add)
elif a<b:
   sub=a-b
   print("The subtraction of two numbers is",sub)
elif a>b:
    match a:
       case 0:
          print("Number is o")
       case 25:
          print("k xa hero!!!")
       case _ if a%2==0:
          print("a$2 is 0") 
       case _:
         print(a)
else:
    mul=a*b
    print("Multiplication of two number is ",mul)