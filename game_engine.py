from player import char_stats
from monster import mons_stats

class Battle:
    def __init__(self, player: char_stats, monster: list):
        self.player = player
        self.monster = monster # List of monster 
        self.level_caps = {1: 20, 2: 50, 3:100}
        
    def fight(self):
        print(f"Battle Start: {self.player.name} VS {len(self.monster)} monsters")
        
        for monster in self.monster:
            print(f"{self.player.name} Fighting With {monster.name}!\n")            
            
            while self.player.hp > 0 and monster.hp > 0:
                # Players Attack
                damage_to_monster = max(0, self.player.atk - monster.df)
                monster.hp -= damage_to_monster
                print(f"{self.player.name} Attacking {monster.name} for {damage_to_monster} Damage.\n Monster HP: {monster.hp} \n==============")
                # Conditional Checking on Monster HP
                if monster.hp <= 0:
                    print(f"{monster.name} Has Slains! | {self.player.name} Wins!")
                    # Monster Die -> EXP to Player
                    self.gain_experience(monster.exp)
                
                # Monster Attack
                damage_to_player = max(0, monster.atk - self.player.df)
                self.player.hp -= damage_to_player
                print(f"{monster.name} Attacking {self.player.name} for {damage_to_player} Damage.\n Player HP: {self.player.hp}\n==============")
                # Conditional Checking on Player HP
                if self.player.hp <= 0:
                    print(f"{self.player.name} Is Defeated by {monster.name} Game Over!")
                    break
                
        # All monster die
        print(f"All monster is defeated! {self.player.name} Wins!")
        
    def gain_experience(self, exp_gained):
        # this function will be used on condition when monster die.
        # Players get the EXP from monster
        self.player.exp += exp_gained # exp_gained will be filled with monster exp later
        
        while self.player.exp >= self.level_caps.get(self.player.lvl, float('inf')):
            self.player.exp -= self.level_caps[self.player.lvl]
            self.player.lvl += 1
            print(f"{self.player.name} Leveled Up! The Level Now Is {self.player.lvl}")
            
            # Additional Stats when player level up
            self.player.atk += 8
            self.player.df  += 4
            self.player.hp  += 15
            print(f"Stats Increased! Attack: {self.player.atk}, Defend: {self.player.df}, HP: {self.player.hp}")