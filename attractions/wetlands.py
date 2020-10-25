class Wetlands:
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animals(self, animal):
        self.animals.append(animal)
