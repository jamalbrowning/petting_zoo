

from models import Barreleye, Bird, Catfish, Donkey, Duck, Goat, Goldfish, Insect, King_Cobra, Kingsnake, Llama, Pig, Sheep, Snake, Whale


def main():
    bassy = Barreleye('Bassy', 'fish', 'Morning', 'Fish chips')
    print(bassy)
    bassy.feed()

    cotters = Bird('Cotters', 'shoebill', 'Evening', 'Bird Food')
    print(cotters)
    cotters.feed()

    catty = Catfish('Catty', 'catfish', 'Afternoon', 'Fish Chips')
    print(catty)
    catty.feed()

    dokay = Donkey('Dokay', 'amiatina', 'Morning', 'Donkey food')
    print(dokay)
    dokay.feed()

    malaard = Duck('Malaard', 'mallard', 'Evening', 'Duck food')
    print(malaard)
    malaard.feed()

    lebron = Goat('Lebron', 'goat', 'Afternoon', 'Goat food')
    print(lebron)
    lebron.feed()

    goldie = Goldfish('Goldie', 'goldfish', 'Evening', 'Fish chips')
    print(goldie)
    goldie.feed()

    scorpie = Insect('Scorpie', 'scorpion', 'Morning', 'Insect food')
    print(scorpie)
    scorpie.feed()

    	
    moonshine = King_Cobra('Moonshine', 'snake', 'Afternoon', 'Snake food')
    print(moonshine)
    moonshine.feed()

    kingsby = Kingsnake('Kingsby', 'snake', 'Morning', 'Snake food')
    print(kingsby)
    kingsby.feed()

    llavya = Llama('Llavya', 'llama', 'Evening', 'Llama food')
    print(llavya)
    llavya.feed()

    pinky = Pig('Pinky', 'Duroc pig', 'Afternoon', 'Pig food')
    print(pinky)
    pinky.feed()

    shep = Sheep('Shep', 'sheep', 'Morning', 'Sheep food')
    print(shep)
    shep.feed()

    anex = Snake('Anex', 'anaconda', 'Evening', 'Snake food')
    print(anex)
    anex.feed()

    swain = Whale('Swain', 'Humpback', 'Afternoon', 'Whale food')
    print(swain)
    swain.feed()
