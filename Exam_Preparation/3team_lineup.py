# def team_lineup(*args):
#     players_info = {}
#
#     for player, country in args:
#         if country not in players_info:
#             players_info[country] = [player]
#         else:
#             players_info[country].append(player)
#
#     sorted_countries = sorted(players_info.keys(), key=lambda x: (-len(players_info[x]), x))
#
#     result = ""
#     for country in sorted_countries:
#         result += f'{country}:\n'
#         for player in players_info[country]:
#             result += f'  -{player}\n'
#
#     return result.strip()
#
# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany"),
#    ("Bruno Fernandes", "Portugal"),
#    ("Bernardo Silva", "Portugal"),
#    ("Harry Maguire", "England")))
#

def team_lineup(*args):
    country_players = {}
    for player_name, country in args:
        if country not in country_players:
            country_players[country] = []  # за да можем да го пълним с играчи
        country_players[country].append(player_name)

    result = ''

    sorted_players = sorted(country_players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for country, players in sorted_players:
        result = f'{country}:\n'
        for player_name in players:
            result += f'  -{player_name}\n'

    return result
