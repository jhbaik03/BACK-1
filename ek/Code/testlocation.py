def find_champion(champion_name, *champion_lists):
    for champion_list in champion_lists:
        if champion_name in champion_list:
            return champion_list.index(champion_name)
    return -1

blueteam_pick = ['Aatrox', 'Jinx', 'Thresh']
blueteam_ban = ['Yasuo', 'Zed', 'Seraphine']
redteam_pick = ['Lee Sin', 'Lux', 'Orianna']
redteam_ban = ['Akali', 'Katarina', 'Darius']

champion_name = 'Lux'
position = find_champion(champion_name, blueteam_pick, redteam_pick, redteam_ban, blueteam_ban)
if position != -1:
    print(f"The champion '{champion_name}' is found at position {position}.")
else:
    print(f"The champion '{champion_name}' is not found.")