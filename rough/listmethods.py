"""
Built-in methods to help manipulating a list
"""

cars = [ "bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")     #2
print(x)

y = cars.pop()
print(y)        #benz
print(cars)

cars.remove("Jeep")
print(cars)     #bmw,honda,audi

slicing = cars[0:2]         #bmw,honda
a = cars[1:]      #honda,audi
print(slicing)
print(a)

print("*#"*20)
print(cars)     #bmw,honda,audi
cars.sort()     #audi,bmw,honda

print(cars)