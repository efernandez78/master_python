def compara_numero (a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("Los parámetros no son enteros.")
    if a>b:
        resultado="a es mayor que b"
    elif a==b:
        resultado="a es igual a b"
    else:
        resultado="a es menor que b"
    return resultado


def compara_cadena(a,b):
    if not isinstance(a,str) or not isinstance(b,str):
        raise TypeError("Los parámetros no son cadenas.")
    if a==b:
        resultado=True
    else:
        resultado=False
    return resultado

