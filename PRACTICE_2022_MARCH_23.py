class Dog:
    def __init__(self, breed, age, coat, stick=None, owner='Sally'):
        self.dogLegs = 4
        self.kindOfDog = breed
        self.age = age
        self.coat = coat
        self.stick = stick
        self.owner = owner

    def get_breed(self):
        return self.kindOfDog

    def set_new_owner(self, owner):
        self.owner = owner

    def give_stick(self, stick):
        self.stick = stick

    def stick_or_no_stick(self, stick_type):
        try:
            self.stick = f'{stick_type}' + self.stick
            print(f"{self.kindOfDog} has {self.stick} stick")
        except:
            print(f"{self.kindOfDog} has no stick!")


c = Dog("German Shepherd", 24, "Black")
g = Dog("Labrador", 24, "Black", owner="Joe")
print(c.dogLegs, c.kindOfDog, c.age, c.coat, c.owner)
print(g.dogLegs, g.kindOfDog, g.age, g.coat, g.owner)
print('')
print(c.dogLegs)

print(c.get_breed())

print(c.owner)
c.set_new_owner("George")
print(c.owner)

c.give_stick('Wooden')

c.stick_or_no_stick('big ')

g.stick_or_no_stick('big ')


print('')

# class Clothing(object):
#     def __init__(self, type, color, size, price=None):
#         self.type = type
#         self.color = color
#         self.size = size
#         self.price = price
#
#     def set_price(self, price):
#         """Set the price of an item of clothing."""
#         self.price = price
#         print(f"Setting the price of the {self.color} {self.type} to ${price}.")
#
#     def get_price(self):
#         """Get the price of an item of clothing, if price is set."""
#         try:
#             print(f"The {self.color} {self.type} costs ${self.price}.")
#         except:
#             print(f"The price of the {self.color} {self.type} hasn't been set yet!")
#     def promote(self, percentage):
#         """Lower the price, if initial price is set."""
#         try:
#             self.price = self.price * (1-percentage/100)
#             print(f"The price of the {self.color} {self.type} has been reduced by {percentage} percent! It now only costs ${self.price:.0f}.")
#         except:
#             print(f"Oops. Set an initial price first!")
#
#
# bluejeans = Clothing("jeans", "blue", 12)
# redtshirt = Clothing("t-shirt", "red", 10, 10)
#
# print("blue jeans -------------------")
# bluejeans.promote(20)
# bluejeans.get_price()
# bluejeans.set_price(30)
# bluejeans.get_price()
# print("red t-shirt ------------------")
# redtshirt.get_price()
# redtshirt.promote(20)