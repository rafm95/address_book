import json


class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail


def name_val(name, contacts):
    for x in contacts:
        if x["name"] in name:
            return False
    return True


def search(search_by, keyword, contacts):
    entries = 0
    for x in contacts:
        if search_by == x[keyword]:
            print("-" * 85)
            print("|Name:  {}   |Phone:  {}    |Email:  {}  |".format(x["name"], x["phone"], x["mail"]))
            print("-" * 85)
            entries += 1
    if entries == 0:
        print("no contacts found")


try:
    with open("contacts.json", "r") as fln:
        dat = json.load(fln)
        contacts = dat["contacts"]
except FileNotFoundError:
    contacts = []
finally:
    if len(contacts) == 0:
        dat = {"contacts": contacts}

print("Hello!!!\nChoose what you want")
while True:
    print("a - Add new contact\ns - Search for contact\ne - Edit contact info\nr - Remove contact\n"
          "q - Quit")
    inp = input("Your choice: ")
    if inp == "q":
        break
    elif inp == "a":
        print("Please, fill following information:")
        while True:
            name = input("Name: ")
            if name_val(name, contacts) is True:
                break
            else:
                if len(name) == 0:
                    print("Name field can't be empty")
                else:
                    print("That name is already exist,wright another name")
        phone = input("Phone: ")
        mail = input("Email: ")
        contacts.append(Contact(name, phone, mail).__dict__)
        print("Contact added")
    elif inp == "s":
        while True:
            while True:
                inp_search = input("n - Search by name\np - Search by phone\nm - Search by mail\na - Show all"
                                   "\nb - Back\nYour choice: ")
                if inp_search in ["n", "p", "m", "b", "a"]:
                    break
                else:
                    print("Choose wright option: ")
            if inp_search == "n":
                name_search = input("Please, enter name: ")
                search(name_search, "name", contacts)
            elif inp_search == "p":
                phone_search = input("Please, enter phone: ")
                search(phone_search, "phone", contacts)
            elif inp_search == "m":
                mail_search = input("Please, enter mail")
                search(mail_search, "mail", contacts)
            elif inp_search == "b":
                break
            elif inp_search == "a":
                if len(contacts) != 0:
                    for x in contacts:
                        print("-" * 85)
                        print("|Name:  {}   |Phone:  {}    |Email:  {}  |".format(x["name"], x["phone"], x["mail"]))
                        print("-" * 85)
                else:
                    print("You have no contacts")
    elif inp == "e":
        while True:
            inp2 = input("Please, enter contact name to change it or press 'B' to go Back: ")
            if name_val(inp2, contacts) is False:
                print("What field would you like to change:\nn - Name\np - Phone\ne - Email\nb - Back")
                inp3 = input("Your choice: ")
                if inp3 == "b":
                    break
                for x in contacts:
                    if x["name"] == inp2:
                        if inp3 == "n":
                            while True:
                                print("Current name: ", x["name"])
                                name_inp = input("Enter new name: ")
                                if name_val(name_inp, contacts) is True:
                                    break
                                else:
                                    print("You already have contact with that name")
                            x["name"] = name_inp
                            print("Contact edited")
                        elif inp3 == "p":
                            print("Current phone: ", x["phone"])
                            x["phone"] = input("Enter new phone: ")
                            print("Contact edited")
                        elif inp3 == "e":
                            print("Current mail: ", x["mail"])
                            x["mail"] = input("Enter new mail: ")
                            print("Contact edited")
            else:
                if inp2 == "B":
                    break
                else:
                    print("You don't have contact with that name")
    elif inp == "r":
        while True:
            inp4 = input("Please, enter contact name to remove it or press 'B' to go Back: ")
            if name_val(inp4, contacts) is False:
                while True:
                    search(inp4, "name", contacts)
                    inp5 = input("Are you sure that you want to remove this contact (y / n) ?")
                    if inp5 == "y":
                        for x in contacts:
                            if x["name"] == inp4:
                                contacts.remove(x)
                                print("Contact removed")
                        break
                    elif inp5 == "n":
                        break
                    else:
                        print("only y or n")
            elif inp4 == "B":
                break
            else:
                print("You don't have contact with that name")
    else:
        print("Wrong input,Try again")

with open("contacts.json", "w") as fl:
    json.dump(dat, fl)