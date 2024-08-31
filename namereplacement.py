def name_replacement():

    str = "Andy came yesterday morning and Andy left today morning"
    name_to_replace = input("Enter name to replace; ")
    name_replacement = input("Enter name replacement; ")
    print(str.replace(name_to_replace, name_replacement))

name_replacement()