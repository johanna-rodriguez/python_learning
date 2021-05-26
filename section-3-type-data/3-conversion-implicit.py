"""
# int / float => float
num_int = 123 # int
num_flo = 1.23 #float
num_new = num_int + num_flo # 124.23 => float
print('type of num_int is : ', type(num_int)) #int
print('type of num_flo is : ', type(num_flo)) # float
print('value of num_new is : ', num_new)      # 124.23
print('type of num_new is : ', type(num_new)) # float
"""
"""
# int / complex
num_int = 123             # int
num_complex = 1.23 + 45j  # complex
num_new = num_int + num_complex # 124.23 + 45j => complex
print('type of num_int is : ', type(num_int)) # int
print('type of num_flo is : ', type(num_complex)) # complex
print('value of num_new is : ', num_new) # 124.23 + 45j
print('type of num_new is : ', type(num_new)) # complex
"""
"""
# int / bool 
value_bool = True # bool => 1 (int)
num_int = 45      # int
num_new = value_bool + num_int # 1 + 45 = 46 => int

print('type of num_int is : ', type(num_int)) # int
print('type of num_flo is : ', type(value_bool)) # bool
print('value of num_new is : ', num_new) # 46
print('type of num_new is : ', type(num_new)) # int
"""
num_int = str(123) 
num_str = '456'
num_new = num_int + num_str
print('type of num_int is : ', type(num_int)) 
print('type of num_str is : ', type(num_str)) 
print('value of num_new is : ', num_new)      
print('type of num_new is : ', type(num_new)) 