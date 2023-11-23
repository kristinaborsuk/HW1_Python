# Дано коло заданої довжини. 
# Необхідно розрахувати сторону квадрату, навколо якого описано коло.
# Також необхідно визначити суму площ квадрату та кола.

from math import pi

circumference = int(input("Enter the radius:"))
radius = (2 * pi) / circumference
square_side = 2 * radius / (2 ** 0.5)
sqare_area = square_side ** 2
circle_area = 2 * pi * radius
sum_ = sqare_area + circle_area
print(f"Square_side: {square_side}\nSum areas: {sum_}")