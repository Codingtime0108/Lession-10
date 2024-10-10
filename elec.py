e = int(input("What is your electricity consumption "))
bill = 0
if e<50:
    bill = (e*2.60)+25
    print("The electricity bill will be:",bill)
elif 50<e<100:
    bill = (e*3.25)+35
    print("The electricity bill will be:",bill)
elif 100<e<200:
    bill = (e*5.26)+45
    print("The electricity bill will be:",bill )
else:
    bill = (e*8.45)+75
    print("The electricity bill will be:",bill)