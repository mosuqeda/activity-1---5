names = ["carlos", "Legaspi", "jang", "maliche"]
user = input("do you want to remove an element by its index or by name (yes/no): ")

print(names)

if user == "yes":
    ask = input("remove a specific data:")
    names.remove(ask)
elif user == "no":
    asking = int(input("what index do you want to remove: "))
    names.pop(asking)

print(names)