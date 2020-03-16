import requests
import random


def poke_types(types):
  type_string = ''
  types_length = len(types)
  if len(types) == 1:
    type_string = f"It has only 1 type which is {types[0]['type']['name'].capitalize()}"
  else:
    type_string = f"It has {types_length} types: "
    for poke_type in types:
      type_string = f"{type_string} {poke_type['type']['name']},"
  print(type_string)


user_pokemon = input('What Pokemon would you like to know about?: ')

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{user_pokemon}',
                        headers={'Accept': 'application/json'})

poke_data = response.json()


print(f'Here is some information obout {user_pokemon}:')
print('')
print(f'Pokemon name: {poke_data["name"]}')
poke_types(poke_data['types'])
