#display menu
def display_menu():
    menu_options=["Add Contact","View Contact","Edit Contact","Delete Contact","List All Contacts","Exit"]
    print("Contact Book Menu:")
    for i, option in enumerate(menu_options, start=1):
        print(f"{i}. {option}")

#add contact

def add_contact(contact_book):
    print("Enter contact name")
    contact_name=str(input())
    print("Enter phone number")
    phone_number=str(input())
    print("Enter email")
    email=str(input())
    print("Enter address")
    address=str(input())
    if contact_name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[contact_name]={
            "phone": phone_number,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

#view contact

def view_contact(contact):
    print("Enter contact to view")
    name=str(input())

    if name in contact:
        print(f"Name: {name}")

        for key,value in contact[name].items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Contact not found!")

#edit contact

def edit_contact(contact_book):
    print("Enter contact to change")
    contact_name=str(input())

    if contact_name in contact_book:
        print("Enter new details for the contact: (leave blank to keep current)")
        phone=str(input())
        print("Enter new email:")
        email=str(input())
        print("Enter new address:")
        address=str(input())

        if phone=="":
            phone=contact_book[contact_name]["phone"]
        if email=="":
            email=contact_book[contact_name]["email"]
        if address=="":
            address=contact_book[contact_name]["address"]
        
        contact_book[contact_name]={
            "phone":phone,
            "email":email,
            "address":address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

#delete contact

def delete_contact(contact_book):
    print("Enter contact to delete")
    contact_name=str(input())
    if contact_name in contact_book:
        confirm = input(f"Are you sure you want to delete {contact_name}? (y/n): ").lower()
        if confirm == "y":
            del contact_book[contact_name]
            print("Contact deleted successfully!")
    else:
        print("Contact not found!")

#list contact

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        print("Here's a list of all contacts: \n")
        for key in contact_book:
            print(f"Name: {key}")
            for keys, values in contact_book[key].items():
                print(f"{keys.capitalize()}: {values}")
            print("")

#final

contact_book={}
while True:
    display_menu()
    print("")
    selection=int(input())

    if selection==1:
        add_contact(contact_book)
        print("")
    elif selection==2:
        view_contact(contact_book)
        print("")
    elif selection==3:
        edit_contact(contact_book)
        print("")
    elif selection==4:
        delete_contact(contact_book)
        print("")
    elif selection==5:
        list_all_contacts(contact_book)
        print("")
    elif selection==6:
        break
