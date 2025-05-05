"#object-oriented-programming-Assignment"
#Assignment 1: Design Your Own Class (Smartphone Example)

#Smartphone Class with Inheritance & Encapsulation

# Parent class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.__storage = storage  # Encapsulated attribute

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage

    def show_info(self):
        print(f"{self.brand} {self.model} with {self.__storage}GB storage")

# Child class
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, refresh_rate):
        super().__init__(brand, model, storage)
        self.refresh_rate = refresh_rate

    def show_info(self):
        super().show_info()
        print(f"Refresh Rate: {self.refresh_rate}Hz - Great for gaming!")
        #Usage of super() to call the parent class method
phone1 = Smartphone("Samsung", "Galaxy A53", 128)
phone2 = GamingPhone("Asus", "ROG Phone 5", 256, 144)

phone1.show_info()
phone2.show_info()


#Activity 2: Polymorphism Challenge (Vehicles Example)

class Vehicle:
    def move(self):
        print("The vehicle moves")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

#Usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
