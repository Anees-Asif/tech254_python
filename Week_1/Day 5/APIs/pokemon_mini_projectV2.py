import requests
import json
import random

# Function to calculate damage in the battle
def calculate_damage(attacker_level, defender_level):
    return random.randint(5, 15) * (attacker_level / defender_level)

# Function to perform a round of battle
def battle_round(attacker, defender):
    damage = calculate_damage(attacker['level'], defender['level'])
    defender['hp'] -= damage
    print(f'{attacker["name"]} attacks {defender["name"]} for {damage:.2f} damage!')
    print(f'{defender["name"]} now has {defender["hp"]:.2f} HP remaining.')

# Function to check if the battle is over
def is_battle_over(user, ai):
    return user['hp'] <= 0 or ai['hp'] <= 0

# Function to swap the attacker and defender
def swap_turn(attacker, defender):
    return defender, attacker

# Function to perform the player's turn
def player_turn(user, ai):
    input('Press Enter to attack...')
    battle_round(user, ai)

# Function to perform the AI's turn
def ai_turn(ai, user):
    battle_round(ai, user)

# Function to display the battle result
def display_battle_result(user, ai):
    if user['hp'] <= 0 and ai['hp'] <= 0:
        print('\nIt\'s a tie! Both Pokémon faint.')
    elif user['hp'] <= 0:
        print(f'\nAI\'s {ai["name"]} defeated your {user["name"]}. Try again!')
    else:
        print(f'\nCongratulations! You defeated AI\'s {ai["name"]}.')

# Function to fetch a list of Pokémon with a random offset
def get_pokemon_list():
    offset = random.randint(1, 200)  # Random offset
    url = f'https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit=10'  # Limiting to 10 Pokémon for simplicity
    response = requests.get(url)
    pokemon_list = json.loads(response.text)['results']
    return pokemon_list

# Get the list of Pokémon
pokemon_list = get_pokemon_list()

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

    # Initialize levels and HP for user and AI
    user_level = random.randint(1, 100)
    ai_level = random.randint(1, 100)
    user_hp = 100.0  # Fixed initial HP for user
    ai_hp = 100.0  # Fixed initial HP for AI

    # Store Pokémon data
    user_pokemon = {"name": user_choice, "level": user_level, "hp": user_hp}
    ai_pokemon = {"name": ai_choice, "level": ai_level, "hp": ai_hp}

    # Start the battle
    print(f'\nYou chose {user_choice} with level {user_level} and {user_hp:.2f} HP.')
    print(f'AI chose {ai_choice} with level {ai_level} and {ai_hp:.2f} HP.')

    while not is_battle_over(user_pokemon, ai_pokemon):
        # Player's turn
        player_turn(user_pokemon, ai_pokemon)

        # Check if the battle is over
        if is_battle_over(user_pokemon, ai_pokemon):
            break

        # AI's turn
        ai_turn(ai_pokemon, user_pokemon)

    # Display the battle result
    display_battle_result(user_pokemon, ai_pokemon)

else:
    print('Invalid choice. Exiting.')
