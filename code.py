class Pokemon:
    def __init__(self, name, level, hp, attack, defense, speed, move_set):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.move_set = move_set
        self.current_hp = hp
    
    def is_alive(self):
        return self.current_hp > 0
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.hp:
            self.current_hp = self.hp

class Move:
    def __init__(self, name, power, accuracy, move_type, pp):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.move_type = move_type  # E.g., "fire", "water", etc.
        self.pp = pp  # Power points (how many times the move can be used)
    
    def use_move(self, attacker, defender):
        # A simple damage calculation formula
        if random.random() <= self.accuracy:
            damage = (attacker.attack - defender.defense) * self.power
            damage = max(damage, 1)  # Minimum damage is 1
            defender.take_damage(damage)
            print(f"{attacker.name} used {self.name}! It dealt {damage} damage.")
        else:
            print(f"{attacker.name} missed the attack!")


def battle(pokemon1, pokemon2):
    # Determine who goes first
    first, second = determine_turn_order(pokemon1, pokemon2)

    # Battle loop
    while pokemon1.is_alive() and pokemon2.is_alive():
        # First Pokémon's turn
        print(f"\n{first.name}'s Turn:")
        move = first.move_set[0]  # Pick the first move for simplicity
        move.use_move(first, second)
        
        # Check if the second Pokémon is knocked out
        if not second.is_alive():
            print(f"{second.name} fainted!")
            print(f"{first.name} wins!")
            break
        
        # Second Pokémon's turn
        print(f"\n{second.name}'s Turn:")
        move = second.move_set[0]  # Pick the first move for simplicity
        move.use_move(second, first)
        
        # Check if the first Pokémon is knocked out
        if not first.is_alive():
            print(f"{first.name} fainted!")
            print(f"{second.name} wins!")
            break



import random



class Pokemon:
    def __init__(self, name, level, hp, attack, defense, speed, move_set):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.move_set = move_set
        self.current_hp = hp
    
    def is_alive(self):
        return self.current_hp > 0
    
    def take_damage(self, damage):
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.hp:
            self.current_hp = self.hp

# Define Moves
tackle = Move("Tackle", 40, 1.0, "normal", 35)
ember = Move("Ember", 40, 1.0, "fire", 25)

# Define Pokémon
pikachu = Pokemon("Pikachu", 5, 35, 55, 40, 90, [tackle, ember])
charmander = Pokemon("Charmander", 5, 39, 52, 43, 65, [tackle, ember])

# Start a battle
battle(pikachu, charmander)


class Move:
    def __init__(self, name, power, accuracy, move_type, pp):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.move_type = move_type  # E.g., "fire", "water", etc.
        self.pp = pp  # Power points (how many times the move can be used)
    
    def use_move(self, attacker, defender):
        # A simple damage calculation formula
        if random.random() <= self.accuracy:
            damage = (attacker.attack - defender.defense) * self.power
            damage = max(damage, 1)  # Minimum damage is 1
            defender.take_damage(damage)
            print(f"{attacker.name} used {self.name}! It dealt {damage} damage.")
        else:
            print(f"{attacker.name} missed the attack!")


def battle(pokemon1, pokemon2):
    # Determine who goes first
    first, second = determine_turn_order(pokemon1, pokemon2)

    # Battle loop
    while pokemon1.is_alive() and pokemon2.is_alive():
        # First Pokémon's turn
        print(f"\n{first.name}'s Turn:")
        move = first.move_set[0]  # Pick the first move for simplicity
        move.use_move(first, second)
        
        # Check if the second Pokémon is knocked out
        if not second.is_alive():
            print(f"{second.name} fainted!")
            print(f"{first.name} wins!")
            break
        
        # Second Pokémon's turn
        print(f"\n{second.name}'s Turn:")
        move = second.move_set[0]  # Pick the first move for simplicity
        move.use_move(second, first)
        
        # Check if the first Pokémon is knocked out
        if not first.is_alive():
            print(f"{first.name} fainted!")
            print(f"{second.name} wins!")
            break
# Define Moves
tackle = Move("Tackle", 40, 1.0, "normal", 35)
ember = Move("Ember", 40, 1.0, "fire", 25)

# Define Pokémon
pikachu = Pokemon("Pikachu", 5, 35, 55, 40, 90, [tackle, ember])
charmander = Pokemon("Charmander", 5, 39, 52, 43, 65, [tackle, ember])

# Start a battle
battle(pikachu, charmander)

    def isAlive(self):
        return self.currentHp > 0



