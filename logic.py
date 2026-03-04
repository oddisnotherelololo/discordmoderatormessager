import aiohttp  # A library for asynchronous HTTP requests
import random
import asyncio
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {"bulbasaur", "eevee", "vulpix"}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['forms'][0]['name']  # Returning a Pokémon's name
                else:
                    return "Pikachu"  # Return the default name if the request fails

    async def info(self):
        # A method that returns information about the pokémon
        if not self.name:
            self.name = await self.get_name()  # Retrieving a name if it has not yet been uploaded
        return f"The name of your Pokémon: {self.name}"  # Returning the string with the Pokémon's name

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    url_image = data['sprites']['front default']
                    print("the code works")
                    return url_image
                else:
                    print("darn it")
                    return None
    async def hurtmode(self, enemy):
        if isinstance(enemy, TungstenWizard):  # Periksa apakah musuh adalah tipe data Penyihir (instance dari kelas Penyihir)
            chance = random.randint(1,5)
            if chance == 1:
                return "Pokemon penyihir menggunakan perisai dalam pertarungan"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pertarungan @{self.pokemon_trainer} dengan @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"@{self.pokemon_trainer} menang melawan @{enemy.pokemon_trainer}!"
    async def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(hours=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Kesehatan Pokemon dipulihkan. HP saat ini: {self.hp}"
        else:
            return f"Kalian dapat memberi makan Pokémon kalian di: {current_time-delta_time}"
class TungstenWizard(Pokemon):
    async def Fireball1(self, enemy):
        FireballPower = random.randint(5,15)
        self.kekuatan += FireballPower
        hasil = await super().attack(enemy)
        self.kekuatan -= FireballPower
        return hasil + f"\nPetarung menggunakan serangan super dengan kekuatan:{FireballPower} "
class ASSassin(Pokemon):
    async def Stab(self, enemy):
        FireballPower = random.randint(6,10)
        self.kekuatan += FireballPower
        hasil = await super().attack(enemy)
        self.kekuatan -= FireballPower
        return hasil + f"\nPetarung menggunakan serangan super dengan kekuatan:{FireballPower} "

async def main():
    wizard = TungstenWizard("username1")
    fighter = ASSassin("username2")
    print(await wizard.info())
    print()
    print(await fighter.info())
    print()
    print(await fighter.attack(wizard))
if __name__ == '__main__':
    asyncio.run(main())
