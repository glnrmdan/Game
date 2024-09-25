from fight import Battle
from player import char_stats
from monster import mons_stats

if __name__ == "__main__":
    # Create a player and a monster
    player = char_stats("Legion Budi", atk=10, df=5, hp=30)
    monster1 = mons_stats("Rikimaru", atk=8, df=4, hp=20)
    monster2 = mons_stats("Treant", atk=15, df=2, hp=20)
    
    monster = [monster1, monster2]
    
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {player.name} Stats")
    player.display_char()
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {monster[0].name} Stats")
    monster1.display_monster()
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {monster[1].name} Stats")
    monster2.display_monster()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    # Initiate battle
    battle = Battle(player, monster)
    battle.fight()