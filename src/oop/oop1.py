# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass
vehicle = Vehicle()
print(vehicle)
class GroundVehicle(Vehicle):
    pass
ground_vehicle = GroundVehicle()
print(ground_vehicle)
class Car(GroundVehicle):
    pass
car = Car()
print(car)
class Motorcycle(GroundVehicle):
    pass
motorcycle = Motorcycle()
print(motorcycle)
class FlightVehicle(Vehicle):
    pass
flight_vehicle = FlightVehicle()
print(flight_vehicle)
class Starship(FlightVehicle):
    pass
starship = Starship()
print(starship)
class Airplane(FlightVehicle):
    pass
airplane = Airplane()
print(airplane)