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
Exercise 2 Round your float up 
"""

import math #Importamos la libreria para poder redondearlo hacia arriba 

# my_float = 3.24 # Numero flotante del ejercicio aterior 

round_float = math.ceil(my_float)# Usamos mat.ceil(x) para poder redondearlo hacia arriba ya que si usamos round(x) no redondea al numero mas cercano 

print('Original number : ', my_float)# Imprimimos el numero original
print('Rounded number :' , round_float) # Imprimimos el nuevo numero redondeado hacia arriba 

"""
Exercise 3 Get the square root of your float
"""

# my_float = 3.23 # Recordamos el numero flotante 

sqrt_float = math.sqrt(my_float) # Usamos math.sqrt ya que es una forma mas clara y directa y como ya tenemos la libreria math no tenemos que volverla a llamar 

print('The square root :',sqrt_float) # Imprimimos nuestra raiz cuadrada 


"""
Exercise 4 Select the first element from your dictionary
"""

