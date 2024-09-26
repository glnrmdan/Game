# parent class
class monster:
    def __init__(self, name):
        self.name = name # Monster Name

# child class
class mons_stats(monster):
    def __init__(self, name, lvl, exp, atk, df, hp):
        super().__init__(name) # call char name from parent class
        # add leveling system and exp point
        self.lvl = lvl   # level
        self.exp = exp   # exp point
        self.atk = atk   # attack
        self.df = df     # defend
        self.hp = hp     # health point
        
    def display_monster(self):
        print(f"Name\t: {self.name}\nLevel\t: {self.lvl}\nEXP\t: {self.exp}\nAttack\t: {self.atk}\nDefend\t: {self.df}\nHP\t: {self.hp}")

# monster_stats = mons_stats("Riki", 15, 5, 10)

# print("=================\nMonster Stats")
# monster_stats.display_monster()
# print("=================")
        