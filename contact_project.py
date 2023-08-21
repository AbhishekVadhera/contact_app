import csv


def load_contacts():
    with open('contact.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        contact_list = list(reader)
        return contact_list


def display_contact(contact_list):
    if not contact_list:
        print('no contact found ')
        return
    else:
        print('CONTACTS : ')
        for contacts in contact_list:
            print('NAME :', contacts[0], 'PHONE_no :', contacts[1])


def add_contact():
    name = input('ENTER CONTACT NAME : ')
    phone_no = input('ENTER PHONE NO : ')
    new_contact = [name, phone_no]
    with open('contact.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(new_contact)
    print('Contact added successfully')


def save_contact(contact_list):
    with open('contact.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for contacts in contact_list:
            writer.writerow(contacts)


def delete_contact(contact_list):
    del_contact = input('ENTER CONTACT NAME TO DELETE : ')
    for contacts in contact_list:
        if contacts[0] == del_contact:
            contact_list.remove(contacts)
            print(contact_list, 'your contact is deleted successfully')
            save_contact(contact_list)


def search_contact(contact_list):
    search_name = input('SEARCH IN NAME CONTACT  : ')
    for contact in contact_list:
        if contact[0] == search_name:
            print('NAME :', contact[0], 'PHONE_no :', contact[1])


def main():
    while True:
        contacts = load_contacts()
        print('_______CONTACT BOOK______')
        print('1. Display all contact ')
        print('2. Add a new contact')
        print('3. Delete a contact ')
        print('4. Search for a contact')
        print('5. Exit the application')
        user_input = int(input('ENTER YOUR NUMBER : '))

        if user_input == 1:
            display_contact(contacts)
        elif user_input == 2:
            add_contact()
        elif user_input == 3:
            delete_contact(contacts)
        elif user_input == 4:
            search_contact(contacts)
        elif user_input == 5:
            print('Exit')
            break
        else:
            print('invalid choice')


main()
