a = input("Do have a medical degree?")
b = int(input("What was your attendence this year?"))
if a == 'Yes':
        print("Allowed")
else:
    if b > 75:
        print("Allowed")
    else:
        print("Not Allowed")