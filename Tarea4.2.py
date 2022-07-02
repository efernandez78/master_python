def es_primo(n): # Definimos primero la función que devuelve True si el numero es primo y False si no lo es
    if n==0 or n==1 or n==2: # Si n es 0,1 o 2 ya sabemos que no es primo, por lo que se devuelve False
        return False   
    for i in range(n-2): #El cuble debe recorrer ahora los números que van desde 2 hasta n-1. Ojo porque por definición i empieza con valor 0.
        if n%(i+2)==0: #No podemos dividir por 0, ni debemos dividir por 1 (el resto es siempre 0 al dividir por 1), por eso dividimos por i+2 (el primer divisor así es 2) y, por eso, en el for el range es hasta n-2.
            return False
    return True

lista=[3,4,8,8,5,5,22,13]
primos=list(filter(es_primo,lista))

print (f"La lista de numeros primos es {primos}.")
