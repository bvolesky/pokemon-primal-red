

battle_tower_folder = r"C:\Users\A2667879\git\pokemon-primal-red\src\data\battle_tower\level_100_mons.h".replace("\\", "/")

#!/usr/bin/env python3
import sys, re

# Gen1 Pokémon set
gen1 = {"BULBASAUR", "IVYSAUR", "VENUSAUR", "CHARMANDER", "CHARMELEON", "CHARIZARD", "SQUIRTLE", "WARTORTLE", "BLASTOISE", "CATERPIE", "METAPOD", "BUTTERFREE", "WEEDLE", "KAKUNA", "BEEDRILL", "PIDGEY", "PIDGEOTTO", "PIDGEOT", "RATTATA", "RATICATE", "SPEAROW", "FEAROW", "EKANS", "ARBOK", "PIKACHU", "RAICHU", "SANDSHREW", "SANDSLASH", "NIDORAN_F", "NIDORINA", "NIDOQUEEN", "NIDORAN_M", "NIDORINO", "NIDOKING", "CLEFAIRY", "CLEFABLE", "VULPIX", "NINETALES", "JIGGLYPUFF", "WIGGLYTUFF", "ZUBAT", "GOLBAT", "ODDISH", "GLOOM", "VILEPLUME", "PARAS", "PARASECT", "VENONAT", "VENOMOTH", "DIGLETT", "DUGTRIO", "MEOWTH", "PERSIAN", "PSYDUCK", "GOLDUCK", "MANKEY", "PRIMEAPE", "GROWLITHE", "ARCANINE", "POLIWAG", "POLIWHIRL", "POLIWRATH", "ABRA", "KADABRA", "ALAKAZAM", "MACHOP", "MACHOKE", "MACHAMP", "BELLSPROUT", "WEEPINBELL", "VICTREEBEL", "TENTACOOL", "TENTACRUEL", "GEODUDE", "GRAVELER", "GOLEM", "PONYTA", "RAPIDASH", "SLOWPOKE", "SLOWBRO", "MAGNEMITE", "MAGNETON", "FARFETCHED", "DODUO", "DODRIO", "SEEL", "DEWGONG", "GRIMER", "MUK", "SHELLDER", "CLOYSTER", "GASTLY", "HAUNTER", "GENGAR", "ONIX", "DROWZEE", "HYPNO", "KRABBY", "KINGLER", "VOLTORB", "ELECTRODE", "EXEGGCUTE", "EXEGGUTOR", "CUBONE", "MAROWAK", "HITMONLEE", "HITMONCHAN", "LICKITUNG", "KOFFING", "WEEZING", "RHYHORN", "RHYDON", "CHANSEY", "TANGELA", "KANGASKHAN", "HORSEA", "SEADRA", "GOLDEEN", "SEAKING", "STARYU", "STARMIE", "MR_MIME", "SCYTHER", "JYNX", "ELECTABUZZ", "MAGMAR", "PINSIR", "TAUROS", "MAGIKARP", "GYARADOS", "LAPRAS", "DITTO", "EEVEE", "VAPOREON", "JOLTEON", "FLAREON", "PORYGON", "OMANYTE", "OMASTAR", "KABUTO", "KABUTOPS", "AERODACTYL", "SNORLAX", "ARTICUNO", "ZAPDOS", "MOLTRES", "DRATINI", "DRAGONAIR", "DRAGONITE", "MEW"}

with open(battle_tower_folder) as f:
    lines = f.readlines()

# Identify header and tail (outer block delimiters)
header, tail = [], []
start, end = None, None
for i, line in enumerate(lines):
    if start is None and line.strip() == "{":
        start = i
    if start is not None and line.strip() == "};":
        end = i
        break
header = lines[:start+1]
tail = lines[end:]
inner = lines[start+1:end]

# Extract blocks using a brace counter
blocks = []
current = []
brace = 0
inside = False
for line in inner:
    if not inside:
        if line.strip().startswith("{"):
            inside = True
            current = [line]
            brace = line.count("{") - line.count("}")
    else:
        current.append(line)
        brace += line.count("{") - line.count("}")
        if brace == 0:
            blocks.append(current)
            inside = False

def get_species(block):
    txt = "".join(block)
    m = re.search(r'\.species\s*=\s*SPECIES_([A-Z0-9_]+)', txt)
    return m.group(1) if m else None

kept = [blk for blk in blocks if (s := get_species(blk)) and s in gen1]

with open(battle_tower_folder, "w") as f:
    f.write("".join(header))
    for blk in kept:
        f.write("".join(blk))
        f.write("\n")
    f.write("".join(tail))
