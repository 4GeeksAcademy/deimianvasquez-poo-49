class Persona():
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.caminando = False
        self.__comiendo = True


    def __str__(self):
        return f"<class 'persona'>"


    def __repr__(self):
        return f"Soy la clase Person"


    def mensaje_presentacion(self):
        return f"Hola soy {self.nombre} {self.apellido}, tengo {self.edad} años de vida y caminando es {self.caminando}"
    
    def caminar(self, data):
        self.caminando = data


class Programador(Persona):
    def __init__(self, nombre, apellido, edad, salario, compañia):
        super().__init__(nombre, apellido, edad)
        self.__salario = salario
        self.compañia = compañia


    def mensaje_presentacion(self):
        return f"Hola soy {self.nombre} {self.apellido}, tengo {self.edad} años de vida y caminando es {self.caminando}, trabajo en {self.compañia} con {self.__salario} de sueldo"
    
    def get_salario(self):
        # aquí tienes logica 
        return self.__salario
    
    def set_salario(self, nuevo_salario):
        self.__salario = nuevo_salario



class Automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def obtener_modelo(self):
        pass



class Auto_familiar(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)


    def obtener_modelo(self):
        return f"El auto familiar tiene un modelo: '{self.modelo}'"



class Auto_deportivo(Automovil):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)


    def obtener_modelo(self):
        return f"El modelo '{self.modelo}' del auto deportivo es el más reciente"


