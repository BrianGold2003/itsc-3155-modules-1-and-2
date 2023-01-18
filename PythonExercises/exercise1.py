#exercise 1
def grade_scale(x):
    if x >= 90:
        return "A"
    elif (x >= 80):
        return "B"
    elif (x >= 70):
        return "C"
    elif (x >= 60 ):
        return "D"
    else:
        return "F"  


x = int(input("Enter a grade from 0 to 100:"))
print("Your grade is " + grade_scale(x))