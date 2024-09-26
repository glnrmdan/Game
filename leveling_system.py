class leveling:    
    def __init__(self, level_caps=None):
        self.level_caps = level_caps if level_caps else {1:20, 2:50, 3:100, 
                                                         4:200, 5:400, 6:800,
                                                         7:1200, 8:1500, 9:2000}
    
    def gain_experience(self, player, exp_gained):
        # this function will be used on condition when monster die.
        # Players get the EXP from monster
        player.exp += exp_gained # exp_gained will be filled with monster exp later
        
        while player.exp >= self.level_caps.get(player.lvl, float('inf')):
            player.exp -= self.level_caps[player.lvl]
            player.lvl += 1
            print(f"{player.name} Leveled Up! The Level Now Is {player.lvl}")
        
        self.stats_bonus(player)
        
    def stats_bonus(self, player):
        # Additional Stats when player level up
        player.atk += 8
        player.df  += 4
        player.hp  += 15
        print(f"Stats Increased! Attack: {player.atk}, Defend: {player.df}, HP: {player.hp}")