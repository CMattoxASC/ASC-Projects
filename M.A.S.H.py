#Mansion,Apartment,Shack,Home
from random import *

myInput = raw_input("Where do you want to live?")
myAccomidations = ["Mansion", "Apartment", "Shack", "Home"]
myAccomidations.append(myInput) 
a = choice(myAccomidations)


myInput = raw_input("What do you want to drive?")
myTesla = ["Model S", "Model X", "Model 3", "Coupe"]
myTesla.append(myInput)
b = choice(myTesla)


myInput = raw_input("Who do you want to be with?")
mySpouse = ["Margot Robbie", "Beyonce", "Nina Agdal", "Elon Musk"]
mySpouse.append(myInput)
c = choice(mySpouse)

myInput = raw_input("What do you want to be?")
myJob = ["Sanitation Engineer", "Rich Dude", "Ugly", "Austin"]
myJob.append(myInput)
d = choice(myJob)


print("You will live in a", a)
print(",and drive a", b)
print("You will be with", c)
print(",but you will only work as", d)