#!/usr/bin/python3
"""Defines a text file-reading function."""

def write_file(filename="", text=""):
    """Write a string to a UTF"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
