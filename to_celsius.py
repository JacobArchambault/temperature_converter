#!/usr/bin/env python
fahrenheit = float(input("What temperature would you like converted from Fahrenheit to Celsius? "))
celsius = round((fahrenheit - 32) * 5 / 9, 2)
print (fahrenheit, "F is", celsius, "C")
