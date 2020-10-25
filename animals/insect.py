from datetime import date
from .Animal import Animal

class Insect(Animal):
    def __init__(self, name, species, shift, food):
        super().__init__(name,species,food)
        self.shift = shift
        self.walking = True
    
    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'
		
Scorpie = Insect('Scorpie', 'scorpion', date.today())
