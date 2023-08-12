# AirBnB_clone - The console

The AirBnB_clone project is a python project aim at exploring the basics, intermeiate, and  advanced python, javascript, html, css and sql concepts. It is a journey into web development.

This repository contains the AirBnB project which is the different classes of objects involved and the storage machanisms for object persistency and the console whiwh is a command line interface used to interact with the objects.

## The AirBnB projct

The models package in contain the following modules:
- base_module: This contain the BaseModule clsss which is the base class for the major classes in the project

- user: this contain the User class which implements the functionality for a User object

- city: this contains the City class that implements the city.

Other modules include:
amenity
state
place

- engine: the engine folder contains the the file_storage module that implements the storage machanism fo the project.

## The console
The console module contains implements the HBNBCommand class which inherits the cmd class. it it provide different commands for interacting with the objects.

Usage `./console.py`
The following commands are available:
- `help`: show help massage
- `create <class name>`: create an object of the class.
- `show <class name> <id>`: show the string represantation of the object
- `destroy <class name> <id>: deletes the object
- `all`: prints the string representation of all the objects. or `all `<class name>` prints the string representation of all the class object.
- `update <class name> <id> <attribute> <value>'`: updates the object attribute base on the value.
