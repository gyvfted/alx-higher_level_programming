#!/usr/bin/python3
"""Defines a file-appending function."""

def append_write(filename="", text=""):
    """Appends a string of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
