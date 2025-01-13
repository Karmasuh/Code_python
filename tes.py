import random

class Pokemon:
    def __init__(self, name, hp, atk, defence, spAtk, spDef, spe, ability, level, exp, condition, maxExp=100):
        self.name = name
        self.level = level
        self.exp = exp
        self.ability = ability
        self.condition = condition
        self.maxExp = maxExp
        self.stats = {
            'hp': hp,
            'atk': atk,
            'defence': defence,
            'spAtk': spAtk,
            'spDef': spDef,
            'spe': spe,
            'hpIv': random.randrange(0, 32),
            'atkIv': random.randrange(0, 32),
            'defenceIv': random.randrange(0, 32),
            'spAtkIv': random.randrange(0, 32),
            'spDefIv': random.randrange(0, 32),
            'speIv': random.randrange(0, 32),
        }

    def statsCalculator(self, stat):
        if stat == 'hp':
            return ((2 * self.stats['hp'] + self.stats['hpIv']) * self.level) // 100 + self.level + 10
        elif stat == 'def':
            return ((2 * self.stats['defence'] + self.stats['defenceIv']) * self.level) // 100 + 5
        elif stat == 'atk':
            return ((2 * self.stats['atk'] + self.stats['atkIv']) * self.level) // 100 + 5
        elif stat == 'spDef':
            return ((2 * self.stats['spDef'] + self.stats['spDefIv']) * self.level) // 100 + 5
        elif stat == 'spAtk':
            return ((2 * self.stats['spAtk'] + self.stats['spAtkIv']) * self.level) // 100 + 5
        elif stat == 'spe':
            return ((2 * self.stats['spe'] + self.stats['speIv']) * self.level) // 100 + 5

    def levelUp(self):
        exp_needed = int(0.8 * (self.level ** 3))
        if self.exp >= exp_needed:
            self.level += 1
            self.exp -= exp_needed
            print(f"{self.name} leveled up! Now at level {self.level}")
        return self.level

    def gainExp(self, amount):
        self.exp += amount
        self.levelUp()

    def newMove(self):
        # Define when a Pokémon learns a new move (based on level and moveset)
        pass  # This can be expanded with move learning logic.

    def abilities(self):
        if self.ability == "Overgrow":
            if self.condition == "LowHP":
                print(f"{self.name}'s Overgrow ability activates!")
        # Add more abilities here.


class Moves:
    def __init__(self, name, element, typing, power, accuracy, pp, effect):
        self.name = name
        self.element = element
        self.typing = typing
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.effect = effect

    def enoughPP(self):
        return self.pp > 0

    def moveDmgCalculator(self, attacker, receiver):
        hitOrMiss = random.randrange(0, 100)
        if hitOrMiss > self.accuracy:
            return f"{attacker.name} missed the attack!"

        damage = (((2 * attacker.level / 5) + 2) * self.power * attacker.statsCalculator('atk') // receiver.statsCalculator('def')) // 50 + 2
        damage *= random.uniform(0.85, 1)  # Random damage factor

        if self.typing == "Physical" and attacker.condition == "Burned":
            damage *= 0.5
        if self.typing == "Special" and attacker.condition == "Burned":
            damage *= 0.5

        return damage


class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def turnOrder(self):
        if self.pokemon1.stats['spe'] > self.pokemon2.stats['spe']:
            return self.pokemon1, self.pokemon2
        elif self.pokemon1.stats['spe'] < self.pokemon2.stats['spe']:
            return self.pokemon2, self.pokemon1
        else:
            return self.pokemon1, self.pokemon2  # Tie case

    def actualCombat(self):
        pokemon1, pokemon2 = self.turnOrder()
        print(f"Battle between {pokemon1.name} and {pokemon2.name}")
        while pokemon1.stats['hp'] > 0 and pokemon2.stats['hp'] > 0:
            print(f"{pokemon1.name} attacks {pokemon2.name}!")
            # Here, you'd apply move and damage logic based on chosen moves.
            # For simplicity, just using a basic attack here.
            move = pokemon1.moves[0]  # Assume the first move is used.
            damage = move.moveDmgCalculator(pokemon1, pokemon2)
            pokemon2.stats['hp'] -= damage
            print(f"{pokemon2.name} took {damage} damage!")

            if pokemon2.stats['hp'] <= 0:
                print(f"{pokemon2.name} fainted!")
                break

            # Switch to pokemon2's turn, repeat similar actions.
            pokemon1, pokemon2 = pokemon2, pokemon1  # Alternate turns

    def winOrLose(self):
        if self.pokemon1.stats['hp'] > 0:
            print(f"{self.pokemon1.name} wins!")
        else:
            print(f"{self.pokemon2.name} wins!")

    def gainEXP(self):
        # Assume the winner gets experience based on battle mechanics.
        if self.pokemon1.stats['hp'] > 0:
            exp_gain = int(1.25 * (self.pokemon1.level ** 3))
            self.pokemon1.gainExp(exp_gain)
            print(f"{self.pokemon1.name} gained {exp_gain} EXP!")


class Items:
    def __init__(self, type, amount=0):
        self.type = type
        self.amount = amount

    def healerItems(self, pokemon):
        if self.type == "Heal":
            pokemon.stats['hp'] += 50  # Example healing amount
            print(f"{pokemon.name} was healed!")
        elif self.type == "PP":
            print(f"{pokemon.name}'s PP was restored!")
        elif self.type == 


# Example usage
pokemon1 = Pokemon(name="Bulbasaur", hp=45, atk=49, defence=49, spAtk=65, spDef=65, spe=45, ability="Overgrow", level=5, exp=100, condition="Healthy")
pokemon2 = Pokemon(name="Charmander", hp=39, atk=52, defence=43, spAtk=60, spDef=50, spe=65, ability="Blaze", level=5, exp=100, condition="Healthy")

combat = Combat(pokemon1, pokemon2)
combat.actualCombat()
