#input, adult or an child, eligble for driving?voting
print("We will find out if you can enroll in a certain class or not")
age = int(input("Enter the student's age: "))
if 10 <= age <= 20:
        print ("Enrolment Allowed")
        if age >= 18:
                print("Wow u can drive too!!!")
        elif age < 18:
                print("Ohh, you can enroll but you aren't a adult yet!")
else:
        print ("Enrolment Not Allowed")