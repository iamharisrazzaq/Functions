

def say_hello():
    print("Hello Haris")
    print("Hello Computer")
    
say_hello()
say_hello()
say_hello()
say_hello()

# Function parameter, and Function argument

def calculate_percentage(obt_marks, total_marks):
    percentage=(obt_marks/total_marks)*100
    print( percentage)

calculate_percentage(858, 1100)
calculate_percentage(800, 1100)
calculate_percentage(750, 1100)


# Make function for Bmi Calculate
def calculate_bmi(weight, height):
    bmi=weight/(height**2)
    print(bmi)
    if(bmi<18.5):
        print("Underweight")
    elif(bmi>=18.5 and bmi<=25):
        print("Normal weight")
    elif(bmi>24.5 and bmi<=29.9):
        print("Overweight")
    elif(bmi>30 and bmi<=39.9):
        print("Overweight")
    else:
        print("Saverly Obese")

calculate_bmi(94, 1.74)

# Checking Eligibility for Voting
def check_eligibility(Birth_year):
    age=2026-Birth_year
    if(age>=18):
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")

check_eligibility(2000)
check_eligibility(2010)