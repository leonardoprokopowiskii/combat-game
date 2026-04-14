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
    
    def receive_attack(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0
    
    def attack(self, target):
        damage = self.__level * 2
        target.receive_attack(damage)
        print(f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")

    
class Hero(Character):
    def __init__(self, name, life, level, ability):
        super().__init__(name, life, level)
        self.__ability = ability

    def get_ability(self):
        return self.__ability
    
    def display_details(self):
        return f"{super().display_details()}\nHabilidade: {self.get_ability()}\n"
    
    def special_attack(self, target):
        damage = self.get_level() * 5 # Increased damage
        target.receive_attack(damage)
        print(f"{self.get_name()} usou a habilidade especial '{self.get_ability()}' em {target.get_name()} e causou {damage} de dano!")
    

class Enemy(Character):
    def __init__(self, name, life, level, enemy_type):
        super().__init__(name, life, level)
        self.__enemy_type = enemy_type

    def get_type(self):
        return self.__enemy_type
    
    def display_details(self):
        return f"{super().display_details()}\nTipo: {self.get_type()}\n"
    

class Game:
    """ Game orchestrator class """
    def __init__(self):
        self.hero = Hero(name="Herói", life=100, level=5, ability="Super Força")
        self.enemy = Enemy(name="Morcego", life=80, level=5, enemy_type="Voador")

    def combat_init(self):
        """ Manage the battle in turns """
        print("----- Iniciando batalha -----")
        while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
            print("\nDetalhes dos Personagens: ")
            print(self.hero.display_details())
            print(self.enemy.display_details())

            input("Pressione Enter para atacar...")
            choice = input("Escolha: 1 - Ataque Normal | 2 - Ataque Especial: ")

            if choice == "1":
                self.hero.attack(self.enemy)
            elif choice == "2":
                self.hero.special_attack(self.enemy)
            else:
                print("Escolha inválida. Escola novamente!")

            if self.enemy.get_life() > 0:
                # Enemy attack hero
                self.enemy.attack(self.hero)

        if self.hero.get_life() > 0:
            print("\nParabéns, você venceu a batalha!")
        else:
            print("\nVocê foi derrotado!")


# Create instance of game and combat init
game = Game()
game.combat_init()