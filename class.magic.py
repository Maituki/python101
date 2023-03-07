
# herencia y encapsulación con atributos y metodos con __ (double underscore)
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.__salary = salary
        print("initializing")

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.__salary)
    
    def __str__(self):
      return "here i am"

class Programador(Employee):
  
  def __init__(self, name, salary, lenguaje):
    super().__init__(name, salary) # llamar el contructor de su padre
    self.lenguaje = lenguaje

java = Programador("jon", 10000, "java")
print(java.name, java.lenguaje)
python = Programador("maria", 50000, "python")



    
# magic functions, dunder functions o métodos dunder, Métodos especiales 
# deberian ejecutarlos implícitamente
# mas información: https://www.tutorialsteacher.com/python/magic-methods-in-python

# dir - devuelve todos los propiedades y métodos de un objeto
print(dir(int))
print(dir(list))

class User:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  # funciones mágicas
  def __str__(self):
    return f"nombre: {self.nombre}, " \
      f"edad: {self.edad}"
    
  # __eq__, __ne__, __lt__, __gt__, __le__, __ge__
  def __eq__(self, otro):
    return self.edad == otro.edad
    
jon = User(nombre="jon", edad=35)
maria = User(nombre="maria", edad=35)

print(jon.nombre, jon.edad)
print(maria)
print(dir(User))
print(jon == maria)
print(jon.__str__()) # es posible, pero no recomendable




# fijate en el uso de pi, un atributo del Clase

class Circulo(object):
  pi = 3.14159

  def __init__(self, radio):
    self.radio = radio

  def area(self):
    # prueba 1
    return Circulo.pi * self.radio * self.radio
    # prueba 2
    return self.pi * self.radio * self.radio
  
# pruebas - ¿qué ocurre con prueba 1 y prueba 2?
c1 = Circulo(10)
c1.pi = 55
print(c1.area())

c2 = Circulo(10)
c2.pi = 55
print(c2.area())



# Tienda de mascotas
class Perro:

  def __init__(self, nombre, edad, raza):
    self.nombre = nombre
    self.edad = edad
    self.raza = raza

perros =[] 

if __name__ == "__main__":
  miles = Perro("Miles", 4, "Jack Russell Terrier")
  buddy = Perro("Buddy", 9, "Dachshund")
  jack = Perro("Jack", 3, "Bulldog")
  jim = Perro("Jim", 5, "Bulldog")

  perros.append(miles)
  perros.append(buddy)
  perros.append(jack)
  perros.append(jim)

  for p in perros:
    print(f"El perro se llama {p.nombre} y es {p.raza}")
