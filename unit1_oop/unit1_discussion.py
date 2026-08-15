"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    """Represents a generic vehicle with basic identifying information."""

    vehicle_type = "Generic Vehicle"  # class variable shared by all instances

    def __init__(self, make, model):
        self.make = make   # instance variable
        self.model = model  # instance variable

    def display_info(self):
        """Return a string describing this vehicle."""
        return f"{self.vehicle_type}: {self.make} {self.model}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    """Represents a car that extends the base vehicle with additional details."""

    vehicle_type = "Car"  # overrides parent class variable
    num_wheels = 4        # new class variable

    def __init__(self, make, model, year, color, features=None):
        super().__init__(make, model)
        self.year = year    # new instance variable
        self.color = color  # new instance variable
        # Nested mutable data used later in the copy demonstration
        self.features = features if features is not None else []

    def display_info(self):
        """Override parent method to include car-specific details."""
        return (
            f"{self.vehicle_type}: {self.year} {self.make} {self.model} "
            f"({self.color}, {self.num_wheels} wheels)"
        )

    def add_feature(self, feature):
        """Add a feature to this car's feature list."""
        self.features.append(feature)
        return f"Added '{feature}' to {self.make} {self.model}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    car1 = ChildClass("Toyota", "Camry", 2022, "Blue", ["Bluetooth"])
    car2 = ChildClass("Honda", "Civic", 2021, "Red", ["Sunroof"])

    # Access class variable through the class itself
    print(f"Class access  -> ChildClass.num_wheels = {ChildClass.num_wheels}")
    print(f"Class access  -> ChildClass.vehicle_type = {ChildClass.vehicle_type}")

    # Access the same class variable through an object
    print(f"Object access -> car1.num_wheels = {car1.num_wheels}")
    print(f"Object access -> car2.vehicle_type = {car2.vehicle_type}")

    # Add a new attribute to only one object after creation
    car1.owner = "Alex"
    print(f"\nAdded 'owner' attribute only to car1: car1.owner = {car1.owner}")
    print(f"car2 has 'owner' attribute: {hasattr(car2, 'owner')}")

    # Display each object's instance namespace
    print(f"\ncar1 instance namespace (__dict__): {car1.__dict__}")
    print(f"car2 instance namespace (__dict__): {car2.__dict__}")

    # Display information about the class namespace
    print(f"\nChildClass namespace (__dict__ keys): {list(ChildClass.__dict__.keys())}")
    print(f"ParentClass namespace (__dict__ keys): {list(ParentClass.__dict__.keys())}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Ford", "Mustang", 2023, "Black", ["Leather Seats", "Navigation"]
    )

    # Shallow copy: creates a new object but shares references to nested mutable data
    shallow = copy(original)

    # Deep copy: creates a new object AND recursively copies nested mutable data
    deep = deepcopy(original)

    print("Before modification:")
    print(f"  Original:      features = {original.features}")
    print(f"  Shallow copy:  features = {shallow.features}")
    print(f"  Deep copy:     features = {deep.features}")

    # Modify the original object's nested mutable data
    original.features.append("Turbo Engine")

    print("\nAfter appending 'Turbo Engine' to original.features:")
    print(f"  Original:      features = {original.features}")
    print(f"  Shallow copy:  features = {shallow.features}")  # also changed (shared list)
    print(f"  Deep copy:     features = {deep.features}")     # unchanged (independent list)

    # Shallow copy also shares top-level references; deep copy creates independent attributes
    original.color = "White"
    print("\nAfter changing original.color to 'White':")
    print(f"  Original color:      {original.color}")
    print(f"  Shallow copy color:  {shallow.color}")  # unchanged (separate object, own color attr)
    print(f"  Deep copy color:     {deep.color}")     # unchanged


# Student-created extension:
# A utility function that compares two ChildClass objects and reports their differences.

def compare_vehicles(vehicle_a, vehicle_b):
    """Compare two ChildClass objects and print a summary of differences."""
    print("\n=== Student Extension: Vehicle Comparison ===")
    attrs = ["make", "model", "year", "color", "features"]
    for attr in attrs:
        val_a = getattr(vehicle_a, attr)
        val_b = getattr(vehicle_b, attr)
        status = "SAME" if val_a == val_b else "DIFFERENT"
        print(f"  {attr:10s}: {val_a!r:30s} vs {val_b!r:30s} -> {status}")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    vehicle = ParentClass("Generic", "Transport")
    print(f"\nParent object: {vehicle.display_info()}")

    # Create and test a child object
    car = ChildClass("Tesla", "Model 3", 2024, "White", ["Autopilot", "Heated Seats"])
    print(f"Child object:  {car.display_info()}")
    print(car.add_feature("Premium Sound"))

    # Demonstrate inheritance: child inherits and overrides parent methods
    print(f"\nInheritance demo:")
    print(f"  car.display_info() (overridden):  {car.display_info()}")
    print(f"  isinstance(car, ParentClass):     {isinstance(car, ParentClass)}")
    print(f"  vehicle.display_info() (parent):  {vehicle.display_info()}")

    demonstrate_namespaces()
    demonstrate_copying()

    # Student extension: compare two vehicles
    other_car = ChildClass("Tesla", "Model 3", 2023, "Blue", ["Autopilot"])
    compare_vehicles(car, other_car)


if __name__ == "__main__":
    main()
