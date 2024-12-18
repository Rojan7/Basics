#19) Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
#methods start() and stop(). The Car class should have instances of Engine and Wheel classes
#as attributes. Implement a method start_car() in the Car class which starts the engine and prints
#"Car started".

class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Wheel:
    def __init__(self, type):
        self.type = type

    def start(self):
        print("Wheel started")

    def stop(self):
        print("Wheel stopped")

class Car:
    def __init__(self, engine, wheel):
        self.engine = engine
        self.wheel = wheel

    def start_car(self):
        self.engine.start()
        print("Car started")
        self.wheel.start()

    def stop_car(self):
        self.engine.stop()
        print("Car stopped")
        self.wheel.stop()

engine = Engine("gvjhbkjlk")
wheel = Wheel("Allojm,y")
car = Car(engine, wheel)

car.start_car()
car.stop_car()