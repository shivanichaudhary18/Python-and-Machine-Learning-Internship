import datetime

def calculate_age(birth_year):
    current_year = datetime.date.today().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("You are", age, "years old.")