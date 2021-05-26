# int
s = "100" 
# conversion del string a entero base 2 (binario)
c = int(s, 2)
print('string converted to int base 2: ', c)
# conversion del string a entero base 10 (numero normal)
c = int(s)
print('string converted to int base 10: ', c)

# str
print("int => string: ", str(10))
print("float => sting: ", str(10.0))
print("complex => string: ", str(10 + 2839j))
# "10"
# "10.0"
# "10 + 2839j
"""
#list
print("string => list: ", list('johanna rodriguez'))
print("int (a str) => list: ", list(str(1254678)))
print("tuple => list: ", list(tuple('johanna')))

string => list: ['a', 'n', 'a', 'r', 't', 'z']
int (convertido a str) => list: ['1', '2']
tuple => list:   ['1', '2']

# set
print("string => set:  ", set('johanna'))
print("int (a str) =>  set:  ", set(str(12)))
print("tuple => set:  ", set(tuple('johanna')))

string => set:   {'j', 'o', 'h', 'a', 'n', 'n', 'a'}
int (a str) => set: {'1', '2'}
tuple => set  {'j', 'o', 'h', 'a', 'n', 'n', 'a'}

# hexadecimal
s = 18  # 10010 => 0001  0010
c = hex(s) #Convierte el 18 en valor hexadecimal
print("Valor Hexadecimal de 18 : ", c) # 0x12

# octal
s = 18  # 10010 => 010 010
c = oct(s) #Convierte el 18 en un valor octal
print("Valor Octal de 18 : ", c)
# 0o22 (octal) <===== 010010 (en binario)
"""