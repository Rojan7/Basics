#input percentage
#> = 80 distinction 
# >=65 → First Division
# >=55 → Second Division
# >=40 → Third Division
# <40 → Fail

percentage = int(input("Enter your percentage"))
def check_grade(percentage):
    if percentage >= 80 and percentage <= 100:
        print (f"{percentage} is Distinction")
    elif percentage >= 65:
        print(f"{percentage} is First Division")
    elif percentage >= 55:
        print(f"{percentage} is Second Division")
    elif percentage >= 40:
        print(f"{percentage} is Third Division")
    else:
        print("Fail")
check_grade(percentage)