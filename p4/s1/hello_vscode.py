while True:

    editor = input("Editor: ")

    standardized = editor.lower()

    # get rid of case check, and see if it is vscode
    if standardized == "visual studio code":
        print("an excellent choice!")
        break
    elif editor == "Word" or editor == "Notepad":
        print("awful")
    else:
        print("not good")


