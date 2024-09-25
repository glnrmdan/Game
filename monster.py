# parent class
class monster:
    def __init__(self, name):
        self.name = name # Monster Name

# child class
class mons_stats(monster):
    def __init__(self, name, atk, df, hp):
        super().__init__(name)
        self.atk = atk  # Attack
        self.df = df    # Defend
        self.hp = hp    # Health Point
        
    def display_monster(self):
        print(f"Name\t: {self.name}\nAttack\t: {self.atk}\nDefend\t: {self.df}\nHP\t: {self.hp}")

# monster_stats = mons_stats("Riki", 15, 5, 10)

# print("=================\nMonster Stats")
# monster_stats.display_monster()
# print("=================")
        