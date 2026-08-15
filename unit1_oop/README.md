# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Running the Program

From this directory, run:

```bash
python3 unit1_discussion.py
```

The program prints output for each section: parent/child object creation, inheritance, namespace demonstration, copy demonstration, and the student extension.

---

## Implementation Documentation

This section documents the completed implementation in `unit1_discussion.py`. The design uses a **Vehicle / Car** hierarchy to model real-world objects while satisfying all assignment requirements.

### Design Summary

| Component | Name | Purpose |
|-----------|------|---------|
| Parent class | `ParentClass` | Generic vehicle with `make` and `model` |
| Child class | `ChildClass` | Car that extends `ParentClass` with year, color, and features |
| Namespace demo | `demonstrate_namespaces()` | Shows class vs instance namespaces |
| Copy demo | `demonstrate_copying()` | Compares shallow and deep copy behavior |
| Student extension | `compare_vehicles()` | Compares two `ChildClass` objects attribute by attribute |

### TODO 1: `ParentClass`

Represents a generic vehicle.

**Class variable**
- `vehicle_type = "Generic Vehicle"` — shared across all instances

**Instance variables**
- `make` — manufacturer name
- `model` — model name

**Methods**
- `__init__(self, make, model)` — constructor
- `display_info(self)` — returns a formatted string describing the vehicle

**Example output**
```
Generic Vehicle: Generic Transport
```

### TODO 2: `ChildClass(ParentClass)`

Represents a car that inherits from `ParentClass`.

**Class variables**
- `vehicle_type = "Car"` — overrides the parent class variable
- `num_wheels = 4` — new class variable

**Instance variables**
- `year` — model year
- `color` — exterior color
- `features` — list of optional features (nested mutable data, used in the copy demo)

**Methods**
- `__init__(self, make, model, year, color, features=None)` — calls `super().__init__()` to reuse parent initialization
- `display_info(self)` — **overrides** the parent method to include year, color, and wheel count
- `add_feature(self, feature)` — new method that appends a feature to the `features` list

**Example output**
```
Car: 2024 Tesla Model 3 (White, 4 wheels)
```

### TODO 3: `demonstrate_namespaces()`

Demonstrates the difference between class namespaces and instance namespaces.

**What it does**
1. Creates two `ChildClass` objects (`car1`, `car2`)
2. Accesses class variables through the class (`ChildClass.num_wheels`) and through an instance (`car1.num_wheels`)
3. Adds a new attribute (`owner = "Alex"`) to only `car1` after creation
4. Prints each object's instance namespace via `__dict__`
5. Prints class namespace keys for `ChildClass` and `ParentClass`

**Key takeaway:** Class variables live on the class and are shared; instance variables live on each object. Attributes added to one instance do not appear on others.

### TODO 4: `demonstrate_copying()`

Demonstrates shallow copy vs deep copy using a `ChildClass` object with a nested `features` list.

**What it does**
1. Creates an original `ChildClass` object with a `features` list
2. Creates a shallow copy with `copy(original)`
3. Creates a deep copy with `deepcopy(original)`
4. Modifies `original.features` by appending `"Turbo Engine"`
5. Modifies `original.color` to `"White"`
6. Prints all three objects before and after each change

**Behavior observed**

| Change | Original | Shallow copy | Deep copy |
|--------|----------|--------------|-----------|
| Append to `features` | Updated | Updated (shared list) | Unchanged (independent list) |
| Change `color` | Updated | Unchanged | Unchanged |

**Key takeaway:** A shallow copy creates a new object but shares references to nested mutable data. A deep copy recursively copies nested data, so changes to the original do not affect the deep copy.

### TODO 5: `main()`

Ties everything together.

**What it does**
1. Creates a `ParentClass` object and calls `display_info()`
2. Creates a `ChildClass` object, calls `display_info()`, and calls `add_feature()`
3. Demonstrates inheritance with `isinstance(car, ParentClass)` and compares overridden vs parent `display_info()`
4. Calls `demonstrate_namespaces()` and `demonstrate_copying()`
5. Calls the student extension `compare_vehicles()`

### Student Extension: `compare_vehicles(vehicle_a, vehicle_b)`

A utility function that compares two `ChildClass` objects across `make`, `model`, `year`, `color`, and `features`, printing `SAME` or `DIFFERENT` for each attribute.

This extension demonstrates how OOP design makes it easy to add reusable behavior on top of existing class structures without modifying the core classes.

---

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
