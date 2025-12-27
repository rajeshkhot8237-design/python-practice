print("Your 12th Result")
a=int(input("Enter the mark in English\n"))
b=int(input("Enter the mark in Marathi\n"))
c=int(input("Enter the mark in Chemistry\n"))
d=int(input("Enter the mark in Physics\n"))
e=int(input("Enter the mark in Mathematics\n"))
f=int(input("Enter the mark in Biology\n"))
#All subject marks addition
total_marks =  a+b+c+d+e+f
percentage = (total_marks*100)/600
print(f"Total Marks:\n{total_marks} ")
print(f"Percentage: \n{percentage}")
if percentage > 34.9 :
    print(f"Your total mark is {total_marks} out of 600")
    print(f"Your total percantage is {percentage} %")
    print("Your result is:-Pass")
else :
    print(f"Your total mark is {total_marks} out of 600")
    print(f"Your total Persantage is {percentage} out of 100%")
    print("Your Result is:-Fail")
