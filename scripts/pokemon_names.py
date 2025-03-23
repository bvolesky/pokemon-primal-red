GEN_1_POKEMON = [
    "BULBASAUR", "IVYSAUR", "VENUSAUR",
    "CHARMANDER", "CHARMELEON", "CHARIZARD",
    "SQUIRTLE", "WARTORTLE", "BLASTOISE",
    "CATERPIE", "METAPOD", "BUTTERFREE",
    "WEEDLE", "KAKUNA", "BEEDRILL",
    "PIDGEY", "PIDGEOTTO", "PIDGEOT",
    "RATTATA", "RATICATE",
    "SPEAROW", "FEAROW",
    "EKANS", "ARBOK",
    "PIKACHU", "RAICHU",
    "SANDSHREW", "SANDSLASH",
    "NIDORAN_F", "NIDORINA", "NIDOQUEEN",
    "NIDORAN_M", "NIDORINO", "NIDOKING",
    "CLEFAIRY", "CLEFABLE",
    "VULPIX", "NINETALES",
    "JIGGLYPUFF", "WIGGLYTUFF",
    "ZUBAT", "GOLBAT",
    "ODDISH", "GLOOM", "VILEPLUME",
    "PARAS", "PARASECT",
    "VENONAT", "VENOMOTH",
    "DIGLETT", "DUGTRIO",
    "MEOWTH", "PERSIAN",
    "PSYDUCK", "GOLDUCK",
    "MANKEY", "PRIMEAPE",
    "GROWLITHE", "ARCANINE",
    "POLIWAG", "POLIWHIRL", "POLIWRATH",
    "ABRA", "KADABRA", "ALAKAZAM",
    "MACHOP", "MACHOKE", "MACHAMP",
    "BELLSPROUT", "WEEPINBELL", "VICTREEBEL",
    "TENTACOOL", "TENTACRUEL",
    "GEODUDE", "GRAVELER", "GOLEM",
    "PONYTA", "RAPIDASH",
    "SLOWPOKE", "SLOWBRO",
    "MAGNEMITE", "MAGNETON",
    "FARFETCHD",
    "DODUO", "DODRIO",
    "SEEL", "DEWGONG",
    "GRIMER", "MUK",
    "SHELLDER", "CLOYSTER",
    "GASTLY", "HAUNTER", "GENGAR",
    "ONIX",
    "DROWZEE", "HYPNO",
    "KRABBY", "KINGLER",
    "VOLTORB", "ELECTRODE",
    "EXEGGCUTE", "EXEGGUTOR",
    "CUBONE", "MAROWAK",
    "HITMONLEE", "HITMONCHAN",
    "LICKITUNG",
    "KOFFING", "WEEZING",
    "RHYHORN", "RHYDON",
    "CHANSEY",
    "TANGELA",
    "KANGASKHAN",
    "HORSEA", "SEADRA",
    "GOLDEEN", "SEAKING",
    "STARYU", "STARMIE",
    "MR_MIME",
    "SCYTHER",
    "JYNX",
    "ELECTABUZZ",
    "MAGMAR",
    "PINSIR",
    "TAUROS",
    "MAGIKARP", "GYARADOS",
    "LAPRAS",
    "DITTO",
    "EEVEE", "VAPOREON", "JOLTEON", "FLAREON",
    "PORYGON",
    "OMANYTE", "OMASTAR",
    "KABUTO", "KABUTOPS",
    "AERODACTYL",
    "SNORLAX",
    "ARTICUNO", "ZAPDOS", "MOLTRES",
    "DRATINI", "DRAGONAIR", "DRAGONITE",
    "MEWTWO", "MEW"
]

if __name__ == "__main__":
    import json
    unique_pokemon = set()
    encounters = r"C:\Users\A2667879\git\pokemon-primal-red\src\data\wild_encounters.json".replace('\\','/')
    with open(encounters) as f:
        data = json.load(f)

    fields = [field['type'] for field in data['wild_encounter_groups'][0]['fields']]
    encounters = data['wild_encounter_groups'][0]['encounters']

    for encounter in encounters:
        _map = encounter['map']
        _label = encounter['base_label']

        if (
                'FireRed' in _label and
                not any(island in _map for island in [
                    'MT_EMBER', 'SEVEN_ISLAND', 'ONE_ISLAND', 'TWO_ISLAND',
                    'THREE_ISLAND', 'FOUR_ISLAND', 'FIVE_ISLAND', 'SIX_ISLAND'
                ])
        ):
            for field in fields:
                if field in encounter:
                    mons = encounter[field]['mons']
                    for mon in mons:
                        if mon['species'].upper().replace('SPECIES_','') in GEN_1_POKEMON:
                            unique_pokemon.add(mon['species'].upper().replace('SPECIES_',''))


pokemon_in_game = list(unique_pokemon)

# Get the pokemon from GEN_1_POKEMON that are not in the game
pokemon_not_in_game = [pokemon for pokemon in GEN_1_POKEMON if pokemon not in pokemon_in_game]
print(pokemon_not_in_game)