#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """
    attributes:
        - first_name
        - last_name
        - age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        dic = {}
        for key in attrs:
            if key in self.__dict__:
                dic[key] = self.__dict__[key]
        return dic
