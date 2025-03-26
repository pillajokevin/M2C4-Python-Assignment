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
Exercise 2 
"""