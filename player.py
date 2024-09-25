# parent class
class character:
    def __init__(self, name):
        self.name = name # char name

# child class
class char_stats(character):
    def __init__(self, name, atk, df, hp):
        super().__init__(name) # call char name from parent class
        self.atk = atk   # attack
        self.df = df     # defend
        self.hp = hp     # health point
   
    
    def display_char(self):
        print(f"Name\t: {self.name}\nAttack\t: {self.atk}\nDefend\t: {self.df}\nHP\t: {self.hp}")



# character_stats = char_stats("Budiono", 10, 10, 30)

# character_stats.atk += 10

# print("=================\nCharacter Stats")
# character_stats.display_char()
# print("=================")