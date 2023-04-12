class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        Pokemon.attack += self.attack_boost

    def defense_up(self):
        Pokemon.defense += self.defense_boost

    def health_up(self):
        Pokemon.health += self.health_boost

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}\r\nAttack: {}, Defense: {}, Health: {}".format(self.name, self.p_type, self.level, self.attack, self.defense, self.health)

"""
Output:
Pokemon name: Alomomola, Type: Normal, Level: 9
Attack: 12, Defense: 10, Health: 15
------
Traning:  (10, 'Evolved!')
------
Pokemon name: Alomomola, Type: Normal, Level: 10
Attack: 15, Defense: 12, Health: 20
"""

pokemon = Pokemon('Alomomola', 9)
print(pokemon)
print('------')
print('Traning: ', pokemon.train())
print('------')
print(pokemon)



class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def attack_up(self):
        Grass_Pokemon.attack += self.attack_boost

    def defense_up(self):
        Grass_Pokemon.defense += self.defense_boost

    def health_up(self):
        Grass_Pokemon.health += self.health_boost

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def __init__(self, name, level=5):
        self.name = name
        self.level = level
        self.weak = "Dark"
        self.strong = "Psychic"

    def train(self):
        self.update()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1

        if self.level > 10:
            self.attack_up()

        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return self.name + " knows a lot of different moves!"

"""
Output:
Pokemon name: Petilil, Type: Grass, Level: 9
Attack: 15, Defense: 14, Health: 12
------
Traning:  10
------
Pokemon name: Petilil, Type: Grass, Level: 10
Attack: 15, Defense: 17, Health: 18
------
Traning:  11
------
Pokemon name: Petilil, Type: Grass, Level: 11
Attack: 17, Defense: 20, Health: 24
"""

p1 = Grass_Pokemon('Petilil', 9)
print(p1)
print('------')
print('Traning: ', p1.train())
print('------')
print(p1)
print('------')
print('Traning: ', p1.train())
print('------')
print(p1)


class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"
    weak = "Dark"
    strong = "Psychic"

class Fire_Pokemon(Pokemon):
    p_type = "Fire"
    weak = "Water"
    strong = "Grass" 

class Flying_Pokemon(Pokemon):
    p_type = "Flying"
    weak = "Electric"
    strong = "Fighting"

"""
Output:
Pokemon name: Cofagrigus, Type: Ghost, Level: 10
Attack: 12, Defense: 10, Health: 15
Pokemon name: Reshiram, Type: Fire, Level: 12
Attack: 12, Defense: 10, Health: 15
Pokemon name: Zapdos, Type: Ghost, Level: 9
Attack: 12, Defense: 10, Health: 15
"""

print(Ghost_Pokemon('Cofagrigus', 10))
print(Fire_Pokemon('Reshiram', 12))
print(Ghost_Pokemon('Zapdos', 9))