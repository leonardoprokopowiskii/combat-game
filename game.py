# Character: mother class
# Hero: user-controlled
#enemy: user adversary

class Character:
    def __init__(self, name, life, level):
        self.__name = name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life
    
    def get_level(self):
        return self.__level
    
    def display_details(self):
        return f"Nome: {self.get_name()}\nVida: {self.get_life()}\nNível: {self.get_level()}"
    

class Hero(Character):
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability
    
    def display_details(self):
        return f"{super().display_details()}\nHabilidade: {self.get_ability()}\n"
    

class Enemy(Character):
    def __init__(self, name, life, level, enemy_type):
        super().__init__(name, life, level)
        self.__enemy_type = enemy_type

    def get_type(self):
        return self.__enemy_type
    
    def display_details(self):
        return f"{super().display_details()}\nTipo: {self.get_type()}"
    

heroi = Hero(name="Leozão", life=100, level=5, ability="Super Força")
print(heroi.display_details())
enemy = Enemy(name="Morcego", life=50, level=3, enemy_type="Voador")
print(enemy.display_details())