#learning about Generating Random Values.
import random #this is a built in python built in module.

for i in range(3):
    print(random.random())


for i in range(3):
    print(random.randint(10, 20))


#Practice
members = ['Seiku', 'Beyage', 'Ebrahim', 'Ahamadou', 'Kadijatou', 'Musa']
leader = random.choice(members)
print(leader)


#Practice creating a Dice Game.
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        secound = random.randint(1, 6)
        return first, secound
    

dice = Dice()
print(dice.roll())



name = input('Enter Name=>')
print(name)
