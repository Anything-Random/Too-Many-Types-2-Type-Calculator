from Type_Advantage import *

def parse_types(input_str: str) -> list[str]:
    input_str = input_str.title().strip()
    input_str = input_str.replace(', ', ' ')
    input_str = input_str.replace(',', ' ').strip().split(' ')
    if "Deez" in input_str:
        index = input_str.index('Deez')
        if len(input_str) > index + 1 and input_str[index + 1] == "Nuts":
            input_str[index] = "Deez Nuts"
            input_str.pop(index + 1)
        else:
            raise KeyError
    if "Mystery" in input_str:
        input_str[input_str.index('Mystery')] = "Mystery/Typeless"
    if "Typeless" in input_str:
        input_str[input_str.index('Typeless')] = "Mystery/Typeless"
    if "Vgc" in input_str:
        input_str[input_str.index('Vgc')] = "VGC"
    return input_str

def print_coverage(full_coverage: dict) -> None:
    print(f"Offense Score: {sum(full_coverage.values())}\n")
    match_ups = {}
    for t in full_coverage.keys():
        if full_coverage[t] in match_ups.keys():
            match_ups[full_coverage[t]].append(t)
        else:
            match_ups[full_coverage[t]] = [t]
    match_ups = dict(sorted(match_ups.items()))
    for e in match_ups.keys():
        print(f"{e}x Match-Ups: {len(match_ups[e])}\n{match_ups[e]}\n")

num = {0: "first", 1: "second", 2: "third", 3: "fourth", 4: "fifth", 5: "sixth"}
mode = "initial"
while mode != 'q':
    if mode == "initial" or string[0] == "0":
        mode = input("Enter m for a matchup, d for defence, c for coverage, t for team coverage, or q to quit. You can enter 0 to change modes at any time.\n").lower().strip()
    string = ["0"]
    if mode == "m":
        string[0] = input("Enter attack type(s) (0 to change modes):\n")
        if string[0] != "0":
            string.append(input("Enter defense type(s):\n"))
    elif mode == "c":
        string[0] = input("Enter the type(s) of your pokemon's first attacking move (0 to change modes):\n")
        if string[0] != "0":
            while string[-1] != "1" and len(string) < 4:
                string.append(input("Enter the type(s) of your pokemon's next attacking move (1 to finish):\n"))
            if string[-1] == "1":
                string.pop()
    elif mode == "t":
        string[0] = [input("Enter the type(s) of your first pokemon's first attacking move (0 to change modes):\n")]
        if string[0][0] != "0":
            p = 0
            move = 1
            while p < 6:
                while move < 4:
                    string[p].append(input(f"Enter the type(s) of your {num[p]} pokemon's {num[move]} attacking move (1 to go to next pokemon, 2 to finish):\n"))
                    move += 1
                    if string[p][-1] == "1":
                        string[p].pop()
                        break
                    elif string[p][-1] == "2":
                        break
                if string[p][-1] == "2":
                    string[p].pop()
                    break
                p += 1
                move = 0
                string.append([])
            if len(string[-1]) == 0:
                string.pop()
        else:
            string[0] = "0"
    elif mode == "d":
        string[0] = input("Enter your pokemon's type(s) (0 to change modes):\n")
    if string[0] == "0":
        continue
    try:
        if mode != "t":
            for i in range(len(string)):
                string[i] = parse_types(string[i])
        else:
            for i in range(len(string)):
                for j in range(len(string[i])):
                    string[i][j] = parse_types(string[i][j])
                    if len(string[i][j]) < 1 or len(string[i][j]) > 4:
                        raise ValueError
            print_coverage(team_coverage(string))
        if mode == "m":
            if 1 <= len(string[0]) <= 4 and 1 <= len(string[1]) <= 4:
                print(f"{attack(string[0], string[1]):g}x")
            else:
                print("Error: Enter only 1-4 Pokemon types per move and 1-4 types for defence, each separated by a space and/or comma, or enter 0 to change modes.\n")
        elif mode == "c":
            for m in string:
                if len(m) < 1 or len(m) > 4:
                    raise ValueError
            print_coverage(coverage(string))
        elif mode == "d":
            if 1 <= len(string[0]) <= 4:
                defences = defence(string[0])
                match_ups = {}
                for t in defences.keys():
                    if defences[t] in match_ups.keys():
                        match_ups[defences[t]].append(t)
                    else:
                        match_ups[defences[t]] = [t]
                print(f"Defence Score: {sum(defences.values())}")
                match_ups = dict(sorted(match_ups.items()))
                for effectiveness in match_ups.keys():
                   print(f"{effectiveness}x Match-Ups: {len(match_ups[effectiveness])}\n{match_ups[effectiveness]}\n")
            else:
                print("Error: Enter only 1-4 Pokemon types separated by a space and/or comma, or enter 0 to change modes.\n")
    except KeyError:
        print("Error: Cannot read types.\n")
    except ValueError:
        print("Error: Enter only 1-4 Pokemon types per move, separated by a space and/or comma, or enter 0 to change modes.\n")