# Variables globales sin hacer uso de la palabra "global"
"""
PRIMER CASO CON SOLO VARIABLE GLOBAL
variable__global = "Hola Mundo"

def custom_function():
    print(variable__global)

print("Fuera: " + variable__global)
# Llamar a la funcion para ejecutarla
custom_function()
"""

"""
variable__global = "Hola Mundo"

def custom_function():
    variable__global= "Hola Johanna"
    print(variable__global)
    variable__global= "Hola Jorge"
    print(variable__global)

print("Fuera: " + variable__global)
# Llamar a la funcion para ejecutarla
custom_function()
"""

# Haciendo uso de la palabra clave "global"
name = " Jorge"
def use_global_function_value():
    global name
    name = "Joa Joa Joa"


use_global_function_value()
print("Name: " + name)
