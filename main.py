import pandas as pd
import matplotlib.pyplot as plt

value = float(input('Inserte el valor que usted desea enviar al estudiante: $ '))

print('''Seleccione una opción:
         Normal case  = 1
         Special case = 2
''')
Comission_select = int(input())

# Definicion de los datos de comision
Useless_commision_values = {
    "less_thousand": 0.035,
    "more_thousand": 0.03,
    "anything": 0,
}

automate_selection = Useless_commision_values["less_thousand"] if value <= 999 else Useless_commision_values["more_thousand"]

def switch(Comission_select, automate_selection):
    switcher = {
        1: automate_selection,
        2: Useless_commision_values["anything"]
    }
    return switcher.get(Comission_select, "Invalid option")

Commision = switch(Comission_select, automate_selection)

def calculos_requeridos(Commision, value):
    final_value = value + (value * Commision)
    return final_value

result = calculos_requeridos(Commision, value)
result_rounded = round(result, 2)  # Redondear el resultado a 2 decimales
print(result_rounded)






