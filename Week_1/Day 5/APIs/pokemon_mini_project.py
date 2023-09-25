import requests
import json
import random

# Get the list of Pokémon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text)['results']

# Ask the user to choose a Pokémon
print('Choose your Pokémon:')
for index, pokemon in enumerate(pokemon_list, start=1):
    print(f'{index}. {pokemon["name"]}')

# Get the user's choice
user_choice_index = int(input('Enter the number of your choice: ')) - 1

if 0 <= user_choice_index < len(pokemon_list):
    # Get the user's choice
    user_choice = pokemon_list[user_choice_index]['name']

    # Randomly select a Pokémon for the AI
    ai_choice = random.choice(pokemon_list)['name']

    # Get the user's Pokémon's data from the API
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(user_choice)
    response = requests.get(url)
    user_pokemon_data = json.loads(response.text)

    # To get ability
    user_abilities = user_pokemon_data['abilities'][0]
    user_ability = user_abilities['ability']


    # Print the user's Pokémon's data
    print('Your Pokémon:')
    print('Name: {}'.format(user_pokemon_data['name']))
    print('Ability: {}'.format(user_ability['name']))

    # Get the AI's Pokémon's data from the API
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ai_choice)
    response = requests.get(url)
    ai_pokemon_data = json.loads(response.text)

    # To get ability
    ai_abilities = ai_pokemon_data['abilities'][0]
    ai_ability = ai_abilities['ability']


    # Print the AI's Pokémon's data
    print('\nAI\'s Pokémon:')
    print('Name: {}'.format(ai_pokemon_data['name']))
    print('Ability: {}'.format(ai_ability['name']))

else:
    print('Invalid choice. Exiting.')
