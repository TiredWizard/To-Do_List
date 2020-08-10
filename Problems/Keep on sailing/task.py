# our class Ship
class Ship:
    def __init__(self, name, destination, capacity):
        self.name = name
        self.destination = destination
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        return "The {0} has sailed for {1}!".format(self.name, self.destination)


dest = input()
black_pearl = Ship("Black Pearl", dest, 800)
print(black_pearl.sail())
