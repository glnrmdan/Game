# parent class
class character:
    def __init__(self, name):
        self.name = name # char name

# child class
class char_stats(character):
    def __init__(self, name, lvl, exp, atk, df, hp):
        super().__init__(name) # call char name from parent class
        # add leveling system and exp point
        self.lvl = lvl   # level
        self.exp = exp   # exp point
        self.atk = atk   # attack
        self.df = df     # defend
        self.hp = hp     # health point
    
    def display_char(self):
        print(f"Name\t: {self.name}\nLevel\t: {self.lvl}\nEXP\t: {self.exp}\nAttack\t: {self.atk}\nDefend\t: {self.df}\nHP\t: {self.hp}")



# character_stats = char_stats("Budiono", 10, 10, 30)

# character_stats.atk += 10

# print("=================\nCharacter Stats")
# character_stats.display_char()
# print("=================")