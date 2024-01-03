#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
language that combines remarkable power with very clear syntax"
str = (str[str.find('object-oriented programming'):str.find('object-oriented programming') + len('object:riented programming')] + " " + str[str.find('with'):str.find('with') + len('with')] + " " + str[str.find('Python'):str.find('Python') + len('Python')])
print(str)
