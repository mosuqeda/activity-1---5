list = [10,9,8,7,6,5,4,3,2,1]
questions = input("do you want to clear the list or leave it unchanged(yes/no)?: ")

if questions == "yes":
    list.clear()
else:
    print("done")

    print(list)
