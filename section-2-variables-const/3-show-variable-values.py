int_val, str_val_one, str_val_two, float_number = 1, "333", "AA", 2.22 

# Variable con texto

print("Primer texto: " + str_val_one)

# Combinacion de dos variables de tipo texto
print(str_val_one + str_val_two) # 333AA

# Combinacion de dos variables de tipo numerico
print(int_val + float_number) # 3.22

# Combinacion de dos variables de tipo numerico y tipo string (ERROR!!)
print(str_val_one + str(float_number)) # "333.22"
print("Ultimo texto: " + str(int_val)) # "Ultimo texto: 1"