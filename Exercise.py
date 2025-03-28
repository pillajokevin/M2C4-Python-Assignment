"""
Exercise 1 : Create a list ,tupla ,float ,integer ,decimal , and dictionay
"""
#Create a list 
my_list = [
    'Spoon',
    'Frying pan' ,
    'Pot' , # Cadena de texto
    True ,#Booleanos
    {"Age": 28 , "Name":"Carolina" , "City":"Bilbao"},#Diccionario dentro de una lista 
    12 ,# Numero entero
    3.24 # Numero flotante 
]#Aqui tenemos una lista en la que podemos ver que tenemos varios tipos de Datos

print('My list :',my_list) #Imprime nuestra lista 

#The tuple
my_tuple = ('Python Intro', 'Java Intro' , 'Javascript Intro' , 'C++ Intro')# Hemos creado una tupla (que son inmutables) 

print('My tupla :' ,my_tuple) # Imprime nuestra tupla 

#Float number
my_float= my_list[-1] # Extraemos el numero flotante de nuestra lista 

print('Float Number :', my_float) #Imprime el numero flotante 

#Integer number 
my_integer = my_list[-2] #Extraemos el Numero entero  de la Lista 

print('Integer number :',my_integer)# Imprimimos el numero entero 

#Create a Decimal number 
from decimal import Decimal # Importamos la libreria para manejar decimales con mas precision 

my_decimal = Decimal("29.959") # Usamos una cadena   para  mayor precision  y para evitarnos fallos 

print('My decimal number :',my_decimal) #Imprimimos el numero decimal 

# My dictionary

my_dictionary = my_list[-3] # Extraemos nuestro diccionario de la lista  que tenemos 

print('My dictionary :',my_dictionary) # Imprimimos nuestro diccionario 

"""
Exercise 2 : Round your float up 
"""

import math #Importamos la libreria para poder redondearlo hacia arriba 

# my_float = 3.24 # Numero flotante del ejercicio aterior 

round_float = math.ceil(my_float)# Usamos mat.ceil(x) para poder redondearlo hacia arriba ya que si usamos round(x) no redondea al numero mas cercano 

print('Original number : ', my_float)# Imprimimos el numero original
print('Rounded number :' , round_float) # Imprimimos el nuevo numero redondeado hacia arriba 

"""
Exercise 3: Get the square root of your float
"""

# my_float = 3.23 # Recordamos el numero flotante 

sqrt_float = math.sqrt(my_float) # Usamos math.sqrt ya que es una forma mas clara y directa y como ya tenemos la libreria math no tenemos que volverla a llamar 

print('The square root :',sqrt_float) # Imprimimos nuestra raiz cuadrada 


"""
Exercise 4 : Select the first element from your dictionary
"""

# my_dictionary = {"Age": 28 , "Name":"Carolina" , "City":"Bilbao"} ##Usamos nuestro diccionario para obtener el primer elemento 

#Extraemos la primera clave del diccionario 
first_key = list(my_dictionary.keys())[0] #Convertimos las claves a  lista y tomamos la primera clave  
first_value = my_dictionary[first_key] # Usamos la clave para obtener su valor 

print('First Key:', first_key) # Imprimimos la primera clave 
print('First Value:',first_value)# Imprimimos el primer valor 



"""
Exercise 5 : Select the second element from your tuple . 
"""

# my_tuple = ('Python Intro', 'Java Intro' , 'Javascript Intro' , 'C++ Intro')# Hemos creado una tupla (que son inmutables) 

second_element = my_tuple[1] # Extraemos de nuestra tupla el segundo elemento 

print(second_element)# Imprimimos el segundo elemento de nuestra tupla 


"""
Exercise 6 : Add an element to the end of your list
"""
'''No tenemos que volver a escribir nuestra lista ya que  la tenemos al principio de el codigo '''
my_list.append('Rose') # Agregamos un nuevo elemento al final de nuestra lista 

print("Updated list: ", my_list)# Imprimimos nuestra lista actualizada 

'''En esta segunda manera de poder anadir un nuevo valor , nos seriviria si necesitamos anadir mas de un valor a nuestra lista '''
# my_list += ['Rose'] # Tambien podriamos usar esta forma para poder anadir un elemento a nuestra lista 
# print('Update list :',my_list)


"""
Exercise 7 : Replace the first element in your list. 
"""

my_list[0] = 'Aroz' # Modificamos el  primer elemento de nuestra lista 

print("Updated list :", my_list) #Imprimimos la nueva lista actualizada 


"""
Exercise 8 : Sort your list alphabetically.
"""

order_list = [item for item in my_list if isinstance(item,(str,int,float))] # Creamos una nueva lista quitando el boolean y el diccionario para poder ordenarlo

order_list.sort(key=str) # convertimos los elementos a string antes de ordenarlos 

print('Sorted filtered list :',order_list) # Imprimimos la lista ordenada 


"""
Exercise 9 : Use reassignment to add an element to your tuple. 
"""

my_tuple = list(my_tuple) # Convertimos la tupla en una lista

my_tuple.append('Ruby Intro') # Agregamos el nuevo elemento 

my_tuple = tuple(my_tuple) # Convertimos la lista nuevamente en tupla 

print('Updated tuple',my_tuple) # Imprimimos la nueva tupla