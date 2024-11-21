import aiohttp
import asyncio

async def get_pokemon(number: int):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            pokemon = await response.json()
            return pokemon['name']

async def main():
    tasks = []
    for number_pokemon in range(1, 151):
        tasks.append(get_pokemon(number_pokemon))

    results = await asyncio.gather(*tasks)
    for pokemon in results:
        print(pokemon)

if __name__ == "__main__":
    asyncio.run(main())
