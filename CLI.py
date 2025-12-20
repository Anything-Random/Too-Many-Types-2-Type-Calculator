from Type_Advantage import *

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