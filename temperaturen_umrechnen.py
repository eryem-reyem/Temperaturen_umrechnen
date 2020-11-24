units = {'a' : 'Grad Celsius', 'b' : 'Grad Klevin', 'c' : 'Grad Fahrenheit' }

def get_temp():
    temp = input('Geben Sie eine Temperatur in ' + units[choice_a] + ' ein: ')
    try:
        n = float(temp)
        return n
    except:
        print('Das ist keine gültige Eingabe für eine Temperatur')

def fahrenheit_to_celsius(temp):
    # (°F − 32) × 5/9 = °C
    return (temp - 32) * 5/9

def kelvin_to_celsius(temp):
    # °K - 273.15 = °C
    return temp - 273.15

def celsius_to_fahrenheit(temp):
    # °C * 9/5 + 32 = °F
    return temp * 9/5 +32

def kelvin_to_fahrenheit(temp):
    # (°K - 273,15) * 9/5 + 32 = °F
    return (temp - 273.15) * 9/5 + 32 

def fahrenheit_to_kelvin(temp):
    # (°F − 32) × 5/9 + 273,15 = °K
    return (temp - 32) * 5/9 + 273.15

def celsius_to_kelvin(temp):
    # °C + 273.15 = °K
    return temp + 273.15

if __name__ == '__main__':

    for i in units:
        print(i, units[i])
        
    choice_a = None
    choice_b = None

    while choice_a not in units:
        choice_a = input('Welche Einheit wollen Sie umrechnen? ')
        if choice_a not in units:
            print('Keine gültige Eingabe!')

    while choice_b not in units:
        choice_b = input('In welche Einheit soll umgerechnet werden? ')
        if choice_b not in units: 
            print('Keine gültige Eingabe!')
        if choice_a == choice_b:
            print('Das ist nicht nötig, bitte wählen Sie eine andere Einheit!')
            choice_b = None

    if choice_a == 'a':
        if choice_b == 'b':
            print(celsius_to_kelvin(get_temp()), units[choice_b])
        if choice_b == 'c':
            print(celsius_to_fahrenheit(get_temp()), units[choice_b])

    if choice_a == 'b':
        if choice_b == 'a':
            print(kelvin_to_celsius(get_temp()), units[choice_b])
        if choice_b == 'c':
            print(kelvin_to_fahrenheit(get_temp()), units[choice_b])

    if choice_a == 'c':
        if choice_b == 'a':
            print(fahrenheit_to_celsius(get_temp()), units[choice_b])
        if choice_b == 'b':
            print(fahrenheit_to_kelvin(get_temp()), units[choice_b])