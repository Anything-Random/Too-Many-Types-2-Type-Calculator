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
    print(f"Offense Score: {sum(full_coverage.values())}", full_coverage)
    match_ups = {}
    for t in full_coverage.keys():
        if full_coverage[t] in match_ups.keys():
            match_ups[full_coverage[t]].append(t)
        else:
            match_ups[full_coverage[t]] = [t]
    match_ups = dict(sorted(match_ups.items()))
    for e in match_ups.keys():
        print(f"{e}x Match-Ups: {len(match_ups[e])}\n{match_ups[e]}\n")
    return full_coverage

def defence(types: list[str]) -> dict:
    defences = dict.fromkeys(sheet[types[0]].to_dict(), 0.0)
    match_ups = {}
    for t in defences.keys():
        effectiveness = attack([t], types)
        defences[t] = effectiveness
        if effectiveness in match_ups.keys():
            match_ups[effectiveness].append(t)
        else:
            match_ups[effectiveness] = [t]
    print(f"Defence Score: {sum(defences.values())}")
    match_ups = dict(sorted(match_ups.items()))
    for effectiveness in match_ups.keys():
        print(f"{effectiveness}x Match-Ups: {len(match_ups[effectiveness])}\n{match_ups[effectiveness]}\n")
    return defences

mode = "initial"
while mode != 'q':
    mode = input("Enter m for a matchup, c for coverage, d for defence, or q to quit. You can enter 0 to change modes at any time.\n").lower().strip()
    string = ["0"]
    if mode == "m":
        string[0] = input("Enter attack type(s):\n")
        if string[0] != "0":
            string.append(input("Enter defense type(s):\n"))
    elif mode == "c":
        string[0] = input("Enter the type(s) of your pokemon's first attacking move (0 to change modes):\n")
        if string[0] != "0":
            while string[-1] != "1" and len(string) < 4:
                string.append(input("Enter the type(s) of your pokemon's next attacking move (1 to finish):\n"))
            if string[-1] == "1":
                string.pop()
    elif mode == "d":
        string[0] = input("Enter your pokemon's type(s):\n")
    while string[0] != "0":
        try:
            for i in range(len(string)):
                string[i] = string[i].title().strip()
                string[i] = string[i].replace(', ', ' ')
                string[i] = string[i].replace(',', ' ').strip().split(' ')
                if "Deez" in string[i]:
                    index = string[i].index('Deez')
                    if len(string[i]) > index+1 and string[i][index+1] == "Nuts":
                        string[i][index] = "Deez Nuts"
                        string[i].pop(index+1)
                    else:
                        print("Error: Cannot read types.\n")
                        continue
                if "Mystery" in string[i]:
                    string[i][string[i].index('Mystery')] = "Mystery/Typeless"
                if "Typeless" in string[i]:
                    string[i][string[i].index('Typeless')] = "Mystery/Typeless"
            if mode == "m":
                if 1 <= len(string[0]) <= 4 and 1 <= len(string[1]) <= 4:
                    print(f"{attack(string[0], string[1]):g}x")
                else:
                    print("Error: Enter only 2-8 Pokemon types separated by a space and/or comma, or enter 0 to change modes.\n")
            elif mode == "c":
                err = False
                for s in string:
                    if 1 > len(s) or len(s) > 4:
                        err = True
                if err == False:
                    coverage(string)
                else:
                    print("Error: Enter only 1-4 Pokemon types per move, separated by a space and/or comma, or enter 0 to change modes.\n")
            elif mode == "d":
                if 1 <= len(string[0]) <= 4:
                    defence(string[0])
                else:
                    print("Error: Enter only 1-4 Pokemon types separated by a space and/or comma, or enter 0 to change modes.\n")
        except KeyError:
            print("Error: Cannot read types.\n")
        finally:
            string = ["0"]
            if mode == "m":
                string[0] = input("Enter attack type(s):\n")
                if string[0] != "0":
                    string.append(input("Enter defense type(s):\n"))
            elif mode == "c":
                string[0] = input("Enter the type(s) of your pokemon's first attacking move (0 to change modes):\n")
                if string[0] != "0":
                    while string[-1] != "1" and len(string) < 4:
                        string.append(input("Enter the type(s) of your pokemon's next attacking move (1 to finish):\n"))
                    if string[-1] == "1":
                        string.pop()
            elif mode == "d":
                string[0] = input("Enter your pokemon's type(s):\n")
