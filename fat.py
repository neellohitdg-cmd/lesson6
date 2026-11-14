h=float(input("ur height in cm:"))
hm=h/100
w=float(input("ur weight in kg:"))
BMI=w/(hm**2)
if BMI<18.5:
    print("underweight")
elif BMI>18.5 and BMI<24.9:
    print("normal")
elif BMI>25 and BMI<29.9:
    print("overweight")
elif BMI>30 and BMI<39.9:
    print("obese")
else:
    print("severely obese :/")
        