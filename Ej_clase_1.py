print("Introduccion a clases")
class Animal:
    edad = 3
    raza = "Chihuas"
    comida = "croquetas"
    def come(self):
        print(f"el perro come " + self.comida)    

print(Animal)
print("Creando el objeto de la clase Animal")
perro = Animal()

print(f"Edad del perro: {perro.edad}")
print(f"Raza del perro: {perro.raza}")
perro.come()

