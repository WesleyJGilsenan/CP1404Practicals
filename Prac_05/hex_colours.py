COLOURS = {"Blue2": "#0000ee", "Chartreuse1": "#7fff00", "Chestnut": "#954535", "Cyan1": "#00ffff", "DarkOrange2": "#ee7600", "DeepSkyBlue2": "#00b2ee", "Goldenrod2": "#eeb422", "LawnGreen": "#7cfc00", "Opal": "#a8c3bc", "Ruby": "#e0115f"}

user_selection = input("Input a colour name to find the hex: ")
while user_selection != "":
    print(f" Your colour: {user_selection} has the hex code of {COLOURS.get(user_selection)}")
    user_selection = input("Input a colour name to find the hex: ")
