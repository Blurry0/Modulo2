#Ejercicio de arreglos
#Crea arreglo de 1 a n, se identificara cual numero de ellos son primos
import sys

def Crear_arreglo(n):
    return [i for i in range(1,n+1)] #Creacion de un array que va de 1 a n 

def Identificar_primos (arr):
    arr = Crear_arreglo(int(arr)) #Llama a la funcion Crear_arreglo y guarda el arreglo creado en arr
    
    primos = [arr.pop(0) ] #Elimina el numero 1 del arreglo el cual se ecuentra en el indice 0 y lo agruega a la lista de primos con pop
    
    help = 0 #Inicializo mi variable help, el cual me indicara si el numero es divisible por otro en la lista
    
    for x in arr:
        help = 0 #Cada vez que cambie el numero que estoy checando si es primo reinicializo mi variable help para que si el anterior no era primo
                 # y por lo tanto help > 0 regrese a cero con el nuevo numero a intentar
                 
        for y in arr: #Checo todos los numeros dentro de mi arreglo
        
            if y==x: #Si es el mismo numero que estoy checando lo salto el checar si es primo o no
                continue
            
            if x%y==0: #Si no es el mismo numero y es divisible entre otro numero del arreglo (y) esto me indica que no es primo y por lo tanto sumo 1 a help y salgo de mi funcion for
                help +=1
                break
            
        if help < 1: #Si al terminar de checar todos los numeros del arreglo y help es menor a 1, es decir, no fue divisible el numero (x) entre otro numero del arreglo (y)
                     #esto me indica que es numero primo y lo apendeo a una lista de numeros primos
            primos.append(x)
            
    return primos #Una vez acabando de checar todos los numeros dentro del arreglo me regresa la lista de primos obtenida


print(Identificar_primos(sys.argv[1])) #Imprime la lista de numeros primos que regres la funcion Identificar_primos
                                        #Para introducir el numero al llamarlo de la terminal debe tomar la siguiente forma python3 ex2.py (num)
                                        #Siendo num hasta que numero llegara el arreglo creado