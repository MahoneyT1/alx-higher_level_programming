#!/usr/bin/python3
""" Write a function that returns the dictionary description,
with simple data structure.
"""
def class_to_json(obj):
    return obj.__dict__
