from player import char_stats

class Battle:
    def __init__(self, player: char_stats, monster: list, leveling_system):
        self.player = player
        self.monster = monster # List of monster 
        self.leveling_system = leveling_system
        
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
                    self.leveling_system.gain_experience(self.player, monster.exp)
                    break
                
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
