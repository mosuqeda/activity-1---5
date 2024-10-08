names = ["carlos", "legaspi", "jang", "maliche"]
question = input("do you want to sort the list alphabetically or reverse its order: ")

if question == "sort":
    names.sort()
elif question == "reverse":
    names.reverse()

print(names)