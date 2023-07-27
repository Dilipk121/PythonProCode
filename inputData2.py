marks = int(input("Enter Your Marks "))

if marks >= 80 and marks <= 100 :
    print("Your Grade is A")
elif marks >= 60 and marks <= 79 :
    print("Your Grade is B")
elif marks >= 40 and marks <= 59 :
    print("Your Grade is C")
else:
    print("Your Are FAIL, Try Again")