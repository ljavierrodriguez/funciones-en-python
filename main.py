from datos import employees
from functions import calcular_edad

for employee in employees:
    #birthday = datetime.strptime(employee["birthday"], '%Y-%m-%d')
    #age = datetime.now().year - birthday.year
    age = calcular_edad(employee["birthday"])
    print(f"Your age is: {age}")