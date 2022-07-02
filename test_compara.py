from compara import *
import pytest

def test_mayor():
    assert compara_numero(3,2)=="a es mayor que b"

def test_igual():
    assert compara_numero(2,2)=="a es igual a b"

def test_menor():
    assert compara_numero(2,3)=="a es menor que b"

def test_cadenaigual():
    assert compara_cadena("Hola","Hola")==True

def test_cadenadistinta():
    assert compara_cadena("Hola","Adios")==False

def test_parametro_entero():
    with pytest.raises(TypeError):
        compara_numero("H",4)

def test_parametro_cadena():
    with pytest.raises(TypeError):
        compara_cadena("H",4)
