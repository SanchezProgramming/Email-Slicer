
contactBook_Names = []
contactBook_Address = []
contactBook_Phone = []
contactBook_Email = []



def deleteContact():

    count = 0

    print("\nThese are all the names in contacts.")
    for eachName in contactBook_Names:
        count = count + 1
        print(count, eachName)

    personSelection = int(input("\nEnter a number to delete contact: "))

    personSelection -= 1

    print(contactBook_Names[personSelection], "was deleted from contacts.")

    contactBook_Names.pop(personSelection)
    contactBook_Address.pop(personSelection)
    contactBook_Email.pop(personSelection)
    contactBook_Phone.pop(personSelection)


def updateContact():

    count = 0

    print("\nThese are all the names in contacts.")
    for eachName in contactBook_Names:

        count = count + 1
        print(count, eachName)

    personSelection = int(input("\nEnter a number to update contact: "))

    personSelection -= 1

    contactBook_Names[personSelection] = input("Enter new name: ")
    contactBook_Address[personSelection] = input("Enter new address: ")
    contactBook_Phone[personSelection] = input("Enter new phone: ")
    contactBook_Email[personSelection] = input("Enter new email: ")


def displayContact():

    print("\nDisplaying all contacts.")


    print("\nNames: ")
    for contacts in contactBook_Names:
        print(contacts)

    print("\nAddresses: ")
    for contacts in contactBook_Address:
        print(contacts)

    print("\nPhone:")
    for contacts in contactBook_Phone:
        print(contacts)

    print("\nEmail:")
    for contacts in contactBook_Email:
        print(contacts)

def createContact():

    print("\nCreating new contact.")

    name = input("Enter name: ")
    contactBook_Names.append(name)

    address = input("Enter address: ")
    contactBook_Address.append(address)

    phone = input("Enter phone: ")
    contactBook_Phone.append(phone)

    email = input("Enter email: ")
    contactBook_Email.append(email)

def menu():

    # Give directions to the user
    print("\n===== CONTACT BOOK =====")
    print("1. Create contact")
    print("2. Update contact information")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit program")

    exitProgram = False

    while(exitProgram != True):

        menuSelection = int(input("\nEnter choice: "))

        if (menuSelection == 1):
            createContact()

        elif (menuSelection == 2):
            updateContact()

        elif (menuSelection == 3):
            deleteContact()

        elif (menuSelection == 4):
            displayContact()

        elif (menuSelection == 5):
            print("Closing contact book.")
            exitProgram = True



def main():

    contactBook_Names.append("Raul")
    contactBook_Address.append("3711 Apple St")
    contactBook_Phone.append("281-183-1833")
    contactBook_Email.append("exmaple@example.com")

    menu()

main()