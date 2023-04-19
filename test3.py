import math
number_people = float(input("Enter the number of people: "))
number_slices = float(input("Enter the number of slices in each cake: "))

calculation = number_people / number_slices
print(math.ceil(calculation), "cakes are needed.")