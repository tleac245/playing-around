import numpy
import circumference
import sqlite3
import os

print("Calculating the area  and circumference of a circle.")

radius = float(input("Enter the radius length: "))

area = numpy.pi * radius**2
print("The area is: ", area)
print("The circumference is: ", circumference.calcCircum(radius))

myPath = r'C:\Users\Taylor\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1'
myFile = "Chinook.db"


#conn = sqlite3.connect(os.path.join(myPath, myFile))
conn = sqlite3.connect(r"C:\Users\Taylor\AppData\Roaming\DBeaverData\workspace6\.metadata\sample-database-sqlite-1\Chinook.db")

cur = conn.cursor()
#cur.execute("CREATE TABLE movie(title, year, score);")
res = cur.execute("SELECT name FROM sqlite_master;")
print(res.fetchall())