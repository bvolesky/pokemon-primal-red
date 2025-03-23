w = r"C:\Users\A2667879\git\pokemon-primal-red\src\data\wild_encounters.json".replace(
    '\\', '/')

import json

with open(w) as f:
    data = json.load(f)

# --- Routes and Pokémon to remove ---
route_removals = {
    "MAP_SSANNE_EXTERIOR": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                            "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL"],
    "MAP_SAFARI_ZONE_WEST": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GOLDEEN",
                             "SPECIES_POLIWAG", "SPECIES_DRATINI", "SPECIES_DRAGONAIR"],
    "MAP_SAFARI_ZONE_NORTH": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GOLDEEN",
                              "SPECIES_POLIWAG", "SPECIES_DRATINI", "SPECIES_DRAGONAIR",
                              "SPECIES_SCYTHER", "SPECIES_TAUROS"],
    "MAP_SAFARI_ZONE_EAST": ["SPECIES_MAGIKARP"],
    "MAP_CERULEAN_CAVE_1F": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GOLDEEN",
                             "SPECIES_POLIWAG", "SPECIES_GEODUDE", "SPECIES_DITTO"],
    "MAP_CERULEAN_CAVE_B1F": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GOLDEEN",
                              "SPECIES_POLIWAG"],
    "MAP_CERULEAN_CAVE_2F": ["SPECIES_GEODUDE", "SPECIES_DITTO"],
    "MAP_SEAFOAM_ISLANDS_B2F": ["SPECIES_PSYDUCK", "SPECIES_ZUBAT"],
    "MAP_SEAFOAM_ISLANDS_B3F": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP",
                                "SPECIES_GYARADOS"],
    "MAP_SEAFOAM_ISLANDS_B4F": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP"],
    "MAP_ROUTE4": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                   "SPECIES_KRABBY", "SPECIES_TENTACOOL", "SPECIES_RATTATA"],
    "MAP_ROUTE10": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL"],
    "MAP_ROUTE11": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL"],
    "MAP_ROUTE12": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL",
                    "SPECIES_PIDGEY"],
    "MAP_ROUTE13": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL",
                    "SPECIES_PIDGEY", "SPECIES_DITTO"],
    "MAP_ROUTE19": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL"],
    "MAP_ROUTE20": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS"],
    "MAP_ROUTE21_NORTH": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS"],
    "MAP_ROUTE21_SOUTH": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP"],
    "MAP_ROUTE22": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_POLIWAG", "SPECIES_RATTATA"],
    "MAP_ROUTE23": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_POLIWAG", "SPECIES_RATTATA"],
    "MAP_ROUTE24": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                    "SPECIES_HORSEA", "SPECIES_KRABBY", "SPECIES_TENTACOOL",
                    "SPECIES_PIDGEY"],
    "MAP_ROUTE25": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS"],
    "MAP_PALLET_TOWN": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                        "SPECIES_HORSEA", "SPECIES_KRABBY"],
    "MAP_VIRIDIAN_CITY": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                          "SPECIES_POLIWAG"],
    "MAP_CERULEAN_CITY": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS",
                          "SPECIES_HORSEA"],
    "MAP_VERMILION_CITY": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_HORSEA",
                           "SPECIES_KRABBY"],
    "MAP_CELADON_CITY": ["SPECIES_PSYDUCK"],
    "MAP_FUCHSIA_CITY": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP"],
    "MAP_CINNABAR_ISLAND": ["SPECIES_PSYDUCK", "SPECIES_MAGIKARP", "SPECIES_GYARADOS"],
    "MAP_MT_MOON_1F": ["SPECIES_ZUBAT"],
    "MAP_VICTORY_ROAD_2F": ["SPECIES_ZUBAT"],
    "MAP_VICTORY_ROAD_3F": ["SPECIES_ZUBAT"],
    "MAP_SEAFOAM_ISLANDS_1F": ["SPECIES_ZUBAT"],
    "MAP_SEAFOAM_ISLANDS_B1F": ["SPECIES_ZUBAT"],
    "MAP_SEAFOAM_ISLANDS_B2F": ["SPECIES_ZUBAT"],
    "MAP_SEAFOAM_ISLANDS_B3F": ["SPECIES_ZUBAT"]
}

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
                # Filter out mons to remove
                mons = encounter[field]['mons']
                filtered_mons = [
                    mon for mon in mons
                    if not (_map in route_removals and mon['species'] in route_removals[
                        _map])
                ]
                encounter[field]['mons'] = filtered_mons

#Optional: Save back to file
with open(w, 'w') as f:
    json.dump(data, f, indent=2)
