def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def num_points_per_game(player_name):
    teams = game_dict()
    for team in teams.values():
        for player in team['players']:
            if player['name'] == player_name:
                return player['points_per_game']
    return None  # Return None if the player is not found

# Example usage
print(num_points_per_game("Jarrett Allen"))


def player_age(player_name):
    teams = game_dict()
    for team in teams.values():
        for player in team['players']:
            if player['name'] == player_name:
                return player['age']
    return None  # Return None if the player is not found

# Example usage
print(player_age("Bradley Beal"))


def team_color(team_name):
    teams = game_dict()
    for team in teams.values():
        if team['team_name'] == team_name:
            return team['colors']
    return None  # Return None if the team is not found

# Example usage
print(team_color("Cleveland Cavaliers"))


def team_height(team_name):
    teams = game_dict()
    for team in teams.values():
        if team['team_name'] == team_name:
            total_height = sum(player['height_inches'] for player in team['players'])
            num_players = len(team['players'])
            return total_height / num_players if num_players > 0 else 0
    return None  # Return None if the team is not found

# Example usage
print(team_height("Washington Wizards"))


def team_names():
    teams = game_dict()
    return [teams['home']['team_name'], teams['away']['team_name']]
print

print(team_names()) 

def player_numbers(team_name):
    teams = game_dict()
    for team in teams.values():
        if team['team_name'] == team_name:
            return [player['number'] for player in team['players']]
    return []

# Example usage
print(player_numbers("Cleveland Cavaliers"))


def player_stats(player_name):
    teams = game_dict()
    for team in teams.values():
        for player in team['players']:
            if player['name'] == player_name:
                return player
    return None  # Return None if the player is not found

# Example usage
print(player_stats("Darius Garland"))


def average_rebounds_by_shoe_brand():
    teams = game_dict()
    brand_rebounds = {}

    for team in teams.values():
        for player in team['players']:
            brand = player['shoe_brand']
            rebounds = player['rebounds_per_game']
            if brand in brand_rebounds:
                brand_rebounds[brand].append(rebounds)
            else:
                brand_rebounds[brand] = [rebounds]

    avg_rebounds_by_brand = {}
    for brand, rebounds_list in brand_rebounds.items():
        avg_rebounds_by_brand[brand] = sum(rebounds_list) / len(rebounds_list)

    return avg_rebounds_by_brand

# Example usage
print(average_rebounds_by_shoe_brand())


# def shared_jersey_numbers():
#     home_players = game_dict()["home"]["players"]
#     away_players = game_dict()["away"]["players"]

#     home_numbers = [player["number"] for player in home_players]
#     away_numbers = [player["number"] for player in away_players]

#     shared_numbers = set(home_numbers) & set(away_numbers)

#     if shared_numbers:
#         return shared_numbers
#     else:
#         return None


# print(shared_jersey_numbers())

	



def find_duplicate_jersey_numbers(team_data):
    '''Finding duplicated jersey numbers'''
    jersey_numbers = set()
    duplicate_jersey_numbers = set()

    for team in team_data.values():
        for player in team['players']:
            jersey_number = player['number']
            if jersey_number in jersey_numbers:
                duplicate_jersey_numbers.add(jersey_number)
            else:
                jersey_numbers.add(jersey_number)
            

    return duplicate_jersey_numbers

duplicate_numbers = find_duplicate_jersey_numbers(game_dict())
print("Duplicate jersey numbers:", duplicate_numbers)