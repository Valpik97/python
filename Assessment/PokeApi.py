import requests


class BasePokemon:

    def __init__(self, name: str) -> None:
        self.__name = name

    def __str__(self):
        return f"name:{self.__name}"


class Pokemon(BasePokemon):

    def __init__(self, id: int, name: str, height: int, weight: int) -> None:
        super().__init__(name)
        self.__id = id
        self.__height = height
        self.__weight = weight

    def __str__(self) -> str:
        return f"id:{self.id} \nname:{self.name} \nheight:{self.height} m\n" \
               f"weight:{self.weight} kg"


class PokeApi(Pokemon):

    @classmethod
    def get_pokemon(cls, name_id: str):
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name_id}")
        req.json()['name'] = Pokemon(req.json()['id'], req.json()['name'], req.json()['height'], req.json()['weight'])
        return req.json()['id'], req.json()['name'], req.json()['height'], req.json()['weight']

print(PokeApi.get_pokemon("ditto"))
