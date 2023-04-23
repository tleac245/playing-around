import numpy
import circumference

print("Calculating the area  and circumference of a circle.")

radius = float(input("Enter the radius length: "))

area = numpy.pi * radius**2
print("The area is: ", area)
print("The circumference is: ", circumference.calcCircum(radius))