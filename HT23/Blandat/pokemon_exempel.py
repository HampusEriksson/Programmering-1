import requests

response = requests.get("https://play.pokemonshowdown.com/data/pokedex.json")

info = response.json()

pokemons = []
for pokemon in info:
    # info[pokemon]["tier"] != "Illegal" and 
    if 1<= info[pokemon]["num"] <= 151:
        pokemons.append(info[pokemon]["name"])
 
print(pokemons)