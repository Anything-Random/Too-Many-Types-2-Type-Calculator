import pandas as pd
import math

sheet = pd.read_pickle('Type_Chart_2.pickle')
#types = {i:x for (i,x) in zip(range(len(sheet.columns)), sheet.columns)}
def attack(atks: list[str], defs: list[str]) -> float:
    if 1 > len(defs) > 4 or 1 > len(atks) > 4:
        raise Exception('Error: Please enter between 1-4 types for the attacking move and the defending pokemon.')
    result = 1
    for atk in atks:
        if 'Uno' in defs:
            for t in defs:
                eff = sheet.loc[atk, t]
                if eff == 0:
                    result *= 2
                else:
                    result *= 1/eff
        else:
            for t in defs:
                result *= sheet.loc[atk, t]
    return float(result)

def coverage(moves: list[list[str]]) -> dict:
    coverages = []
    for types in moves:
        effectiveness = []
        for t in types:
            effectiveness.append(sheet.loc[t].to_dict())
        coverages.append({t: math.prod(e[t] for e in effectiveness) for t in effectiveness[0].keys()})
    full_coverage = {t: max(cover[t] for cover in coverages) for t in coverages[0].keys()}
    #print(f"Offense Score: {sum(full_coverage.values())}", full_coverage)
    #match_ups = {}
    #for t in full_coverage.keys():
    #    if full_coverage[t] in match_ups.keys():
    #        match_ups[full_coverage[t]].append(t)
    #    else:
    #        match_ups[full_coverage[t]] = [t]
    #match_ups = dict(sorted(match_ups.items()))
    #for e in match_ups.keys():
    #    print(f"{e}x Match-Ups: {len(match_ups[e])}\n{match_ups[e]}\n")
    return full_coverage

def team_coverage(pokemons: list[list[list[str]]]) -> dict:
    team_coverages = []
    for pokemon in pokemons:
        team_coverages.append(coverage(pokemon))
    full_coverage = {t: max(poke[t] for poke in team_coverages) for t in team_coverages[0].keys()}
    #print(f"Offense Score: {sum(full_coverage.values())}", full_coverage)
    #match_ups = {}
    #for t in full_coverage.keys():
    #    if full_coverage[t] in match_ups.keys():
    #        match_ups[full_coverage[t]].append(t)
    #    else:
    #        match_ups[full_coverage[t]] = [t]
    #match_ups = dict(sorted(match_ups.items()))
    #for e in match_ups.keys():
    #    print(f"{e}x Match-Ups: {len(match_ups[e])}\n{match_ups[e]}\n")
    return full_coverage

def defence(types: list[str]) -> dict:
    defences = dict.fromkeys(sheet[types[0]].to_dict(), 0.0)
    #match_ups = {}
    #for t in defences.keys():
    #    effectiveness = attack([t], types)
    #    defences[t] = effectiveness
    #    if effectiveness in match_ups.keys():
    #        match_ups[effectiveness].append(t)
    #    else:
    #        match_ups[effectiveness] = [t]
    #print(f"Defence Score: {sum(defences.values())}")
    #match_ups = dict(sorted(match_ups.items()))
    #for effectiveness in match_ups.keys():
    #    print(f"{effectiveness}x Match-Ups: {len(match_ups[effectiveness])}\n{match_ups[effectiveness]}\n")
    return defences
