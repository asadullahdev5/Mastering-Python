# Write program using function to convert celcius to farehnheit

def farenheit_to_celcius(farenheit): 
    celcius = 5/9 * (farenheit -32)
    return celcius

F = 97.2
C = farenheit_to_celcius(F)
print(f"{F} Farenheit = {C:.1f} Ceclcius")
