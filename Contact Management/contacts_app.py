"""
Author : Prajval Patel (C0911611)
Date : October 29th, 2023
Program : Personal Contacts Application
"""


def main():
    print('Personal Contacts Application')
    contacts = [
        {
            'contact_id': 1,
            'name': 'Prajval Patel',
            'phone': '123-456-7890',
            'email': 'p.patel@example.com',
            'address': 'Toronto, ON'
        },
        {
            'contact_id': 2,
            'name': 'John Doe',
            'phone': '123-456-7890',
            'email': 'john.doe@example.com',
            'address': 'Quebec'
        }
    ]
    while True:
        user_choice = menu()
        if user_choice == '1':
            readContacts(contacts)
        elif user_choice == '2':
            addContact(contacts)
        elif user_choice == '3':
            updateContact(contacts)
        elif user_choice == '4':
            deleteContact(contacts)
        elif user_choice == '5':
            searchContact(contacts)
        elif user_choice == '6':
            print('Thank you. Visit again!')
            break
        else:
            print('Invalid input, please select valid option')


def menu():
    print('------------------------- \n1. View All Contacts \n2. Add Contact \n3. Update Contact \n4. Delete '
          'Contact \n5. Search Contact \n6. Exit')
    return input('Enter your choice: ')


def readContacts(contacts):
    for contact in contacts:
        print('Name:', contact['name'])
        print('Phone:', contact['phone'])
        print('Email:', contact['email'])
        print('Address:', contact['address'])
        print()


def getNewContactDetails(contact_id):
    # ID is auto-incremented
    contact_id += 1
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email address: ')
    address = input('Enter address: ')

    new_contact = {
        'contact_id': contact_id,
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    return new_contact


def addContact(contacts):
    # ID is calculated based on length of contacts list
    contact_id = len(contacts)
    contact_details = getNewContactDetails(contact_id)
    contacts.append(contact_details)
    repeat_task = input('Want to add more contact? (Y/N): ')
    # Asking user if they want to add more contacts
    if repeat_task == 'Y' or repeat_task == 'Yes' or repeat_task == 'y':
        addContact(contacts)
    else:
        print('Contact has been added successfully. Thank you, visit again!.')


def getContactId(contacts, prompt):
    for contact in contacts:
        print('Id:', contact['contact_id'])
        print('Name:', contact['name'])
        print('Phone:', contact['phone'])
        print('Email:', contact['email'])
        print('Address:', contact['address'])
        print()
    contact_id = input(prompt)

    try:
        contact_id = int(contact_id)
        if contact_id > len(contacts):
            print('Sorry, no contacts found with the given id')
            return
        else:
            return contact_id
    except ValueError:
        print('Invalid input. Contact ID should be an integer.')
        return getContactId(contacts, prompt)


''' Updating contact is performed based on the contact ID
considering the case of having multiple contacts with same name '''


def updateContact(contacts):
    update_prompt = 'Select contact ID to update: '
    contact_to_update = getContactId(contacts, update_prompt)
    for contact in contacts:
        if contact['contact_id'] == contact_to_update:
            print('Select detail to update: \n1. Name \n2. Phone \n3. Email \n4. Address')
            detail_to_update = input('Selection: ')
            if detail_to_update == '1':
                new_name = input('Enter the new name: ')
                contact['name'] = new_name
            elif detail_to_update == '2':
                new_phone = input('Enter the new phone number: ')
                contact['phone'] = new_phone
            elif detail_to_update == '3':
                new_email = input('Enter the new email address: ')
                contact['email'] = new_email
            elif detail_to_update == '4':
                new_address = input('Enter the new address: ')
                contact['address'] = new_address
            else:
                print('Invalid choice. No updates were made.')
                return

            print('Contact has been updated successfully. Thank you, visit again!.')
            return


# Deleting contact is also performed based on the contact ID
def deleteContact(contacts):
    delete_prompt = 'Select contact ID to delete: '
    contact_to_delete = getContactId(contacts, delete_prompt)
    for contact in contacts:
        if contact['contact_id'] == contact_to_delete:
            print('Contact found. Are you sure you want to delete it? (Y/N)')
            confirmation = input()
            if confirmation == 'y' or confirmation == 'yes' or confirmation == 'Y':
                contacts.remove(contact)
                print('Contact deleted successfully.')
                # After deleting a contact, reassigning IDs to maintain continuity
                for i in range(len(contacts)):
                    contacts[i]['contact_id'] = i + 1
                return


def searchContact(contacts):
    search_input = input('Enter name, phone or email of the contact to search: ')
    search_result = []
    for contact in contacts:
        if search_input in contact['name'] or search_input in contact['phone'] or search_input in contact['email']:
            search_result.append(contact)

    if search_result:
        print('Search results:')
        for result in search_result:
            print('Name:', result['name'])
            print('Phone:', result['phone'])
            print('Email:', result['email'])
            print('Address:', result['address'])
            print()
    else:
        print('No matching contacts found.')


main()
