from models import Persona, Programador, Auto_deportivo, Auto_familiar
from ultils import sum


# crear instancia de la clase 
person_one = Persona("Deimian", "Vásquez", "31")
person_two = Persona("Daniela", "Cornejo", "20")

person_three = Programador("Andrés", "Morenio", 19, 1000, "4GeeksAcademy")
person_three.set_salario(2500)
person_three.salario = 10999 # --> no debe pasar

# print(person_three.get_salario())


# print(person_one.mensaje_presentacion())
# print(person_two.mensaje_presentacion())
# print(person_three.mensaje_presentacion())



auto_familiar = Auto_familiar("Ford", "Familiar 2023")

auto_deportivo = Auto_deportivo("Tesla", "Tesla motors sport")


print(auto_familiar.obtener_modelo()) # output: El auto familiar tiene un modelo: 'Familiar 2023'

print(auto_deportivo.obtener_modelo()) # output: El modelo 'Tesla motors sport' del auto deportivo es el más reciente