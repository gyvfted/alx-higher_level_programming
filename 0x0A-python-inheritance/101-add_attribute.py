#!/usr/bin/python3
""Defines a function that adds attributes to objects."""


def add_attribute(obj, name, value):
    """ add_attribute function """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
