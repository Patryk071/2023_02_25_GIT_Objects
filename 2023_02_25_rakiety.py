class Rocket():

    def __init__(self):
        self.altitude = 0

    def move(self):
        self.altitude += 1
        print(self.altitude)


rocket1 = Rocket()
rocket1.move()
print(rocket1.altitude)
rocket1.move()
print(rocket1.altitude)

rocket2 = Rocket()
print(rocket2.altitude)
rocket3 = Rocket()
print(rocket3.altitude)
rocket4 = Rocket()
print(rocket4.altitude)
rocket5 = Rocket()
print(rocket5.altitude)