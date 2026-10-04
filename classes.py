class Point():
    def __init__(self, x ,y):
        self.x = x
        self.y = y


class Flight():
    def __init__(self, capasity):
        self.capasity = capasity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capasity - len(self.passengers)


#p = Point(2, 8)

#print(f"X: {p.x}, Y: {p.y}.")

flight = Flight(3)

#flight.add_passenger(input("Name: "))

#print(f"Free seats: {flight.open_seats()}")

people = ["Harry", "Ron", "Hermione", "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight sucsessfylly!")
    else:
        print("No open seats availeble")

