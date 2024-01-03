#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = (str[str.find('object-oriented programming'):str.find('object-oriented programming') + len('objected oriented programming')] + "with Python")
print(str)
