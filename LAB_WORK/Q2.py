#input percentage
#> = 80 distinction 
# >=65 → First Division
# >=55 → Second Division
# >=40 → Third Division
# <40 → Fail

percentage = int(input("Enter your percentage"))
def check_grade(percentage):
    if percentage >= 80 and percentage <= 100:
        return (f"{percentage} is Distinction")
    elif percentage >= 65:
        return(f"{percentage} is First Division")
    elif percentage >= 55:
        return(f"{percentage} is Second Division")
    elif percentage >= 40:
        return(f"{percentage} is Third Division")
    else:
        return("Fail")
result =  check_grade(percentage)
print(result)