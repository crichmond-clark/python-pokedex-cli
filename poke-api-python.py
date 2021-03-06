import requests
import random

separator = ', '
# Function definitions


def poke_types(types):
  types_string = ''
  types_length = len(types)
  if len(types) == 1:
    types_string = f"It has 1 type: {types[0]['type']['name'].capitalize()}"
  else:
    types_string = f"It has {types_length} types: "
    for poke_type in types:
      types_string = f"{types_string} {poke_type['type']['name'].capitalize()},"
  return types_string


def moves(moves_list):
  move_names = ''
  move_numbers = [random.randint(0, len(moves_list) - 1),
                  random.randint(0, len(moves_list) - 1),
                  random.randint(0, len(moves_list) - 1),
                  random.randint(0, len(moves_list) - 1),
                  ]
  random_moves = [moves_list[index]['move']['name'].capitalize()
                  for index in move_numbers]
  move_names = separator.join(random_moves)
  moves_string = f"""It can learn {len(moves_list)} moves, including:
    {move_names}"""
  return moves_string


def abilities(abilities_list):
  ability_names_list = [abilities_list[index]['ability']['name'].capitalize()
                        for index in range(0, len(abilities_list))]
  ability_names = separator.join(ability_names_list)
  abilities_string = f"""It has {len(abilities_list)} abilites:
    {ability_names}"""
  return abilities_string


def stats(stats_list):
  stats_dict = {}
  count = 0
  for stat in stats_list:
    stat_name = stat['stat']['name']
    stat_level = stat['base_stat']
    stats_dict[count] = {
        'stat': stat_name,
        'level': stat_level
    }
    count += 1
  plain_stats = [f"{stats_dict[index]['stat'].capitalize()}: {stats_dict[index]['level']}" for index in range(
      0, len(stats_dict))]
  stats_string = f"Base stats: {separator.join(plain_stats)}"
  return stats_string


def pokemon_info():
  print(f'Here is some information obout {user_pokemon}:')
  print('')
  print(f'Pokemon name: {poke_data["name"].capitalize()}')
  print('')
  print(poke_types(poke_data['types']))
  print('')
  print(stats(poke_data['stats']))
  print('')
  print(moves_and_abilities)


# API request
user_pokemon = input('What Pokemon would you like to know about?: ')

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{user_pokemon}',
                        headers={'Accept': 'application/json'})

poke_data = response.json()

# Function calls
moves_and_abilities = f"""{moves(poke_data['moves'])}

  and

{abilities(poke_data['abilities'])}"""

pokemon_info()
