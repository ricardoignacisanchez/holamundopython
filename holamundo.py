
from libreria import metodo_auxiliar, funcion, metodo_auxiliar_posterior
from autenticacion import autenticar_usuario

def patata():
    print('e'*1000000*5)

def metodo_ricardo():
    print("método ricardo")

def here(name):
    print(name,'esta dentro')

if __name__ == '__main__':
    print("hola, planeta")
    patata() 
    metodo_ricardo()
    metodo_auxiliar()
    funcion()
    metodo_auxiliar_posterior()
    if autenticar_usuario('pepe', 'test'):
        print("pepe puede entrar")
    else:
        print("pepe no puede entrar")

