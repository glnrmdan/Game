import player
import monster

class leveling:
    def __init__(self, player: player.char_stats, monster: monster.mons_stats):
        self.player = player
    
    def entity_player(self):
        self.character = player.char_stats("Budi", 1, 0, 15, 5, 50)
        
    # def entity_monster(self, monster1):
    #     self.monster1 = monster1.mons_stats("Treant", 1, 10, 5, 5, 20)    


char1 = leveling.entity_player(player.char_stats.display_char())

char1
# character.display_char()
# print("=====================")
# monster1.display_monster()