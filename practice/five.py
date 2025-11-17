class Animal():
    def __init__(self, no_of_legs = 2):
        self.no_of_legs = no_of_legs
        print('animal created')
    
    def eat(self):
        print('i am eating')

    def reveal_legs(self):
        print('i have {} legs'.format(self.no_of_legs))

class Dog(Animal):
    def __init__(self, no_of_legs, name):
        Animal.__init__(self, no_of_legs)
        self.name = name
        print('Dog Created')

    def bark(self):
        print('woof! my name is {}'.format(self.name))
    
    def reveal_legs(self):
        print('I am a dog revealing it\'s legs')

#python doesn't have new keyword
creature = Animal()
creature.eat()
creature.reveal_legs()
tommy = Dog(4, 'tommy')
tommy.bark()
tommy.eat()
tommy.reveal_legs()
