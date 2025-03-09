import math
import numpy as np

class Datos():
    def __init__(self):
        pass
    def ingresar_n(self):
        while True:
            try:
                self.n = int(input("Inserte el valor de n: "))
                break
            except Exception as e:
                print(e)
    def ingresar_a(self):
        while True:
            try:
                self.a = input("Inserte el valor de a: ")
                break
            except Exception as e:
                print(e)
    def ingresar_b(self):
        while True:
            try:
                self.b = input("Inserte el valor de b: ")
                break
            except Exception as e:
                print(e)


class Metodos:
    def __init__(self, n: int, a: str, b: str):
        self.n = n
        self.a = self.convertir_valor(a)
        self.b = self.convertir_valor(b)
        self.k = (self.b - self.a) / self.n

    def convertir_valor(self, valor):
        valor = valor.replace('pi', 'math.pi')
        valor = valor.replace('e', 'math.e')
        return float(eval(valor))
            
    def establecer_funcion(self):

        print("\nMenú de funciones: ")

        funciones = {
            1: 'sinx', 
            2: 'cosx', 
            3: 'e^x', 
            4: 'polinomio'
        }
        
        print(funciones)

        while True:
            try:
                funcion = int(input("\nElija la opción que desea del menú de funciones: "))
            except Exception as e:
                print(e)
                continue
            if funcion not in funciones:
                print("\nLa función ingresada no está dentro del menú de funciones\n")
                continue
            else: 
                break
            
        match funcion:
            case 1:
                return math.sin
            case 2:
                return math.cos
            case 3:
                return math.exp
            case 4:
                gradoPolinomio = int(input("\nInserte el grado del polinomio: "))
                self.coeficientes = []

                for i in reversed(range(gradoPolinomio + 1)):
                    coeficiente = float(input(f"Inserte el coeficiente de x^{i}: "))
                    self.coeficientes.append(coeficiente)

                self.coeficientes.sort(reverse=False) #ordenamiento descendente


                # test = ['sinx', 'cosx', 'e^x']
                # print(dict(enumerate(test))) me devuelve un diccionario con llaves = indice elementos y claves = elemento de la lista

                def polinomio(x):
                    resultado = 0
                    for grado, coef in enumerate(self.coeficientes):
                        resultado += coef * (x ** grado)

                    return resultado
                
                return polinomio
            
class Riemann(Metodos):
    def __init__(self, n: int, a: str, b: str):
        super().__init__(n, a, b)

    def sumatoria_izquierda(self, funcion: Metodos):
        x = np.zeros(self.n) #Para esta sumatoria solo necesito n puntos, si n = 2, necesito 2 puntos: x_0 y x_1 = x_(n-1) para trazar un rectangulo con altura x_0 y otro con altura x_1

        for i in range(0, self.n): #La suma de Riemann por izquierda va desde x_0 hasta x_(n-1)
            x[i] = self.a + self.k * i

        suma = 0
        for i in range(0, self.n):
            suma += funcion(x[i])
        return self.k * suma
    
    def sumatoria_derecha(self, funcion: Metodos):
        x = np.zeros(self.n + 1)

        for i in range(1, self.n + 1): #La suma de Riemann por izquierda va desde x_1 hasta x_(n)
            x[i] = self.a + self.k * i

        suma = 0
        for i in range(1, self.n + 1):
            suma += funcion(x[i])
        return self.k * suma
    
    def sumatoria_medio(self, funcion: Metodos):
        x = np.zeros(self.n + 1) #Si el usuario quiere n = 2 rectangulos, entonces debo tener n+1 = 3 puntos X_i = (x_0, x_1, x_2) para hallar las alturas f(x) en los puntos medios de los intervalos ([x_0, x_1], [x_1, x_2])

        for i in range(0, self.n + 1):
            x[i] = self.a + self.k * i
        
        suma = 0
        for i in range(1, self.n + 1):
            punto_medio = self.a + ((i - 1/2) * self.k) #La demostracion a esta fórmula la hago en el ejercicio 11 de la sección: Ejercicios del libro del pdf en Latex
            suma += funcion(punto_medio)
        return self.k * suma

class Trapecio(Metodos):
    def __init__(self, n: int, a: str, b: str):
        super().__init__(n, a, b)

    def sumatoria(self, funcion: Metodos):
        x = np.zeros(self.n + 1)

        for i in range(0, self.n + 1):
            x[i] = self.a + self.k * i

        suma = 0
        for i in range(1, self.n):
            suma += funcion(x[i])

        return self.k * (((1/2) * funcion(x[0])) + (suma) + ((1/2) * funcion(x[self.n])))

#Para este metodo consulté la fórmula en internet, ya que la demostración es compleja
class Simpson(Metodos):
    def __init__(self, n, a, b):
        if n % 2 != 0: #n tiene que ser par, si es impar se le suma 1
            n = n + 1
        super().__init__(n, a, b)

    def sumatoria(self, funcion: Metodos):
        x = np.zeros(self.n + 1)
        for i in range(0, self.n + 1):
            x[i] = self.a + (self.k * i)

        #Para los impares
        sumaImpares = 0
        for i in range(1, self.n, 2):
            sumaImpares += funcion(x[i])
            # print(f"Impar: {i}")
        
        sumaPares = 0
        for i in range(2, self.n, 2):
            sumaPares += funcion(x[i])
            # print(f"Par: {i}")

        return (self.k / 3) * (funcion(x[0]) + 4*sumaImpares + 2*sumaPares + funcion(x[self.n]))



condiciones = Datos()

condiciones.ingresar_n()
condiciones.ingresar_a()
condiciones.ingresar_b()


aproxRiemann = Riemann(condiciones.n, condiciones.a, condiciones.b)
fx = Metodos(condiciones.n, condiciones.a, condiciones.b).establecer_funcion()
print("\nSumas de Riemann: ")
print(f"Aproximación por izquierda: {aproxRiemann.sumatoria_izquierda(fx)}")
print(f"Aproximación por derecha: {aproxRiemann.sumatoria_derecha(fx)}")
print(f"Aproximación por punto medio: {aproxRiemann.sumatoria_medio(fx)}")

aproxTrapecio = Trapecio(condiciones.n, condiciones.a, condiciones.b)
print("\nMétodo del Trapecio: ")
print(f"Aproximación: {aproxTrapecio.sumatoria(fx)}")

aproxSimpson = Simpson(condiciones.n, condiciones.a, condiciones.b)
print("\nMétodo de Simpson: ")
print(f"Aproximación: {aproxSimpson.sumatoria(fx)}")


# print(Simpson(condiciones.n, condiciones.a, condiciones.b).n)
# print(Metodos(1, '1', '3').convertir_valor('pi*7'))