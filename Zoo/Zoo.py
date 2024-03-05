class Animal:
    def __init__(self, name, age, health=100, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10


class Lion(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=90, happiness=60)
        self.roar_sound = "Roar!"

    def roar(self):
        print(self.roar_sound)


class Tiger(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=80, happiness=70)
        self.stripe_color = "Orange"

    def show_stripes(self):
        print(f"{self.name} has {self.stripe_color} stripes.")


class Bear(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, health=70, happiness=80)
        self.fish_eater = True

    def eat_fish(self):
        if self.fish_eater:
            print(f"{self.name} is enjoying some fresh fish!")
            self.feed()


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name, age):
        self.animals.append(Lion(name, age))

    def add_tiger(self, name, age):
        self.animals.append(Tiger(name, age))

    def add_bear(self, name, age):
        self.animals.append(Bear(name, age))

    def print_all_info(self):
        print("-" * 30, self.name, "-" * 30)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala", 5)
zoo1.add_lion("Simba", 3)
zoo1.add_tiger("Rajah", 4)
zoo1.add_tiger("Shere Khan", 6)

zoo1.print_all_info()