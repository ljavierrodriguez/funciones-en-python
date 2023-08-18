from datetime import datetime

def calcular_edad(date):
    birthday = datetime.strptime(date, '%Y-%m-%d')
    age = datetime.now().year - birthday.year
    return age