# Aplicando buenas practicas Parte 1 

# 1.- Uso de la sangria

if 5 > 2:
    print("Mensaje de 5 mayor a 2")
    
    
    # 2.- Codigo maximo por linea 79 caracteres maximo
    print("hbdsjhbjshbffdgfgddfjsdnfdnfnfnfnfnfnfnnfnffmdfnfvnvnfjknfknvdfkndfndkfvnkfnfjkvnfjnfnfkjnfkjnkfvnjvnkjfn"+ 
          "kjfnvkjfnkjnffkjvkfvfknjvfnjfnkfkvjfnfjvdfknjknjkfdnjnkfvfndvnjfnvkdjvnjkfnjkvdnjfdnjfjfdnkdfdnjfndvfns")
    # Codigo de comentario por linea 72 caracteres maximo

    # 3.- Saltos de linea

    # 3.1.- Clases

    class MyClass:
        # 3.1.1.- Class functions
        def first_function():
            return "first"

        def second_function():
            return "second"

# 3.2.- Principal functions 
def principal_function():
    print("Principal function")

# 4.- Aplicando lower_snake_case a la funcion 
def second_function():
    print("Principal function")

# Aplicando una variable

lower_snake_case_value = 2

# 5.- Clase nombre aplica UpperCase

class SecondClass:
        def _private_function():
            print("Private function")

        def public_function():
            print("public function")

# 6.- Sumas 
one = 1
two = 344
three = 10
total = ( one
        + two
        - three)
# 335


one = "111"
two = "344"
three = "333333"
total = ( one
        + two
        - three)
print(total) # 1111344333333