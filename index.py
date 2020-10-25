from animals import Barreleye, Bird, Catfish, Donkey, Duck, Goat, Goldfish, Insect, King_Cobra, Kingsnake, Llama, Pig, Sheep, Snake, Whale
from attractions import Petting_Zoo, Snake_Pit, Wetlands

bassy = Barreleye('Bassy', 'fish', 'Morning', 'Fish chips', 12345)
cotters = Bird('Cotters', 'shoebill', 'Evening', 'Bird Food')
catty = Catfish('Catty', 'catfish', 'Afternoon', 'Fish Chips')
dokay = Donkey('Dokay', 'amiatina', 'Morning', 'Donkey food')
malaard = Duck('Malaard', 'mallard', 'Evening', 'Duck food')
lebron = Goat('Lebron', 'goat', 'Afternoon', 'Goat food')
goldie = Goldfish('Goldie', 'goldfish', 'Evening', 'Fish chips')
scorpie = Insect('Scorpie', 'scorpion', 'Morning', 'Insect food') 
moonshine = King_Cobra('Moonshine', 'snake', 'Afternoon', 'Snake food')
kingsby = Kingsnake('Kingsby', 'snake', 'Morning', 'Snake food')
llavya = Llama('Llavya', 'llama', 'Evening', 'Llama food')
pinky = Pig('Pinky', 'Duroc pig', 'Afternoon', 'Pig food')
shep = Sheep('Shep', 'sheep', 'Morning', 'Sheep food')
anex = Snake('Anex', 'anaconda', 'Evening', 'Snake food')
swain = Whale('Swain', 'Humpback', 'Afternoon', 'Whale food')

varmint_village = Petting_Zoo("Varmint Village", "Pet all you can!")
reptilian_corner = Snake_Pit("Reptilian Corner", "Lots and Lots and Lots of Reptiles")
the_wet_place = Wetlands("The Wet Place", "It's wet here.")

varmint_village.add_animals([dokay,cotters,malaard,lebron,llavya,pinky,shep,swain])
reptilian_corner.add_animals([scorpie,moonshine,kingsby,anex])
the_wet_place.add_animals([catty,goldie,swain])

print(the_wet_place)
