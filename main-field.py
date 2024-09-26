from game_engine import Battle
from player import char_stats
from monster import mons_stats

if __name__ == "__main__":
    # Create a player and a monster
    player = char_stats("Legion Budi", 1, 0, atk=10, df=5, hp=40)
    monster1 = mons_stats("Rikimaru",1, 10, atk=8, df=4, hp=20)
    monster2 = mons_stats("Treant",1, 20, atk=15, df=2, hp=20)
    monster3 = mons_stats("Mimic",3, 100, 1, 8, 50)
    
    monster = [monster1, monster2, monster3]
    
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {player.name} Stats")
    player.display_char()
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {monster[0].name} Stats")
    monster1.display_monster()
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {monster[1].name} Stats")
    monster2.display_monster()
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {monster[2].name} Stats")
    monster3.display_monster()
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    
    # Initiate battle
    battle = Battle(player, monster)
    battle.fight()
    
    print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=\nThe {player.name} Stats After Battle")
    player.display_char()