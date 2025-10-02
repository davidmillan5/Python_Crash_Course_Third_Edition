## Modifying Element In A List

motorcycles = ["honda", "yamaha", "kawasaki", "suzuki"]

print(motorcycles)

motorcycles[0] = "ducati"

print(motorcycles)

## Adding Elements To A List

## Append To The End Of A List

motorcycles.append('ducati')
print(motorcycles)

cars = []

cars.append("Honda")
cars.append("Maseratti")
cars.append("Mercedes")
cars.append("Lamborghini")
cars.append("Citroen")

print(cars)


## Inserting Elements Into A List

motorcycles.insert(0,"ducati")
print(motorcycles)

## Removing Elements From A List

del motorcycles[0]
print(motorcycles)


## Removing An Item Using The pop()

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

## Popping From Any Position On The List

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

## Removing An Item By Value
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

too_expensive = 'kawasaki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")