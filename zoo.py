class Zookeeper:
    def __init__(self, name):
        self.name = name

    def clean_enclosure(self, enclosure):
        print("f{self.name} is cleaning enclosure")
        enclosure.clean()

    def animal_feed(self, animal):
        print(f"{self.name} is feeding {animal.name}")
        animal.feed()

class Enclosure:
    def __init__(self):
        self.animal = []
        self.is_clean = False
        self.is_open = False

    def add_animal(self, animal):
        self.animal.append(animal)

    def remove_animal(self, animal):
        self.animal.remove(animal)

    def clean(self):
        self.is_clean = True
        print("enclosure is clean")

    def open(self):
        self.is_open = True
        print("enclosure is open")

    def close(self):
        self.is_open = False
        print("enclosure is closed")

class Animal:
    def __init__(self, name):
        self.name = name
        self.hungry = True
        self.happy = False

    def feed(self):
        if self.hungry:
            self.hungry = False
            self.happy = True
            print(f"{self.name} is fed and happy")
        else:
            print(f"{self.name} is not hungry")

    def rest(self):
        if not self.hungry:
            print(f"{self.name} is resting")
        else:
            print(f"{self.name} cannot rest because its hungry")



if __name__ == "__main__":
    zookeeper = Zookeeper("Peter")
    enclosure = Enclosure()
    Kapibara = Animal("Kapibara")
    Lion = Animal("Lion")
    Monkey = Animal("Monkey")

    enclosure.add_animal(Kapibara)
    enclosure.add_animal(Lion)
    enclosure.add_animal(Monkey)
    enclosure.open()

    choice = input("1 - Clean the enclosure\n2 - Feed an animal\n3 - let animal rest\n4 - Close the enclosure\n\n choose an action:  ")
    if choice == "1":
        zookeeper.clean_enclosure(enclosure)
    elif choice == "2":
        animal_name = input("enter animal name you want to feed: ")
        for animal in enclosure.animal:
            if animal.name.lower() == animal_name.lower():
                zookeeper.animal_feed(animal)
    elif choice == "3":
        animal_name = input("enter animal name you'll let rest: ")
        for animal in enclosure.animal:
            if animal.name.lower() == animal_name.lower():
                animal.rest()
    elif choice == "4":
        enclosure.close()
