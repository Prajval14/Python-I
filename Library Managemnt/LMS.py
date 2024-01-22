"""
Author : Prajval Patel (C0911611)
Program : Library Management System
"""

import os


def main():
    print('Library Management System')

    # Check if file exist in the provided directory
    file_path = input('Enter file path: ')
    if not os.path.exists(file_path):
        print('Sorry, requested file does not exist. Try again.')
        return main()

    while True:
        user_choice = menu()
        if user_choice == '1':
            readBooks(file_path)
        elif user_choice == '2':
            addBook(file_path)
        elif user_choice == '3':
            updateBook(3, file_path)
        elif user_choice == '4':
            updateBook(4, file_path)
        elif user_choice == '5':
            searchBook(file_path)
        elif user_choice == '6':
            print('Thank you. Visit again!')
            break
        else:
            print('Invalid input, please select valid option')


def menu():
    print(
        '------------------------- \n1. Display All Books \n2. Add Book \n3. Borrow Book \n4. Return Book \n5. Search '
        'Book \n6. Exit')
    return input('Enter your choice: ')


def addBook(file_path):
    with open(file_path, 'r') as file_data:
        book_count = 0
        for line in file_data:
            book_count += 1

    with open(file_path, 'a') as file_data:
        book_name = input('Enter the name of book: ')
        book_author = input('Enter the author of book: ')
        book_availability = 'Yes'
        new_content = f'\n{book_count + 1}, {book_name}, {book_author}, {book_availability}'
        file_data.write(new_content)
        print('Book has been added successfully. Thank you, visit again!.')
        file_data.close()


def readBooks(file_path):
    print('Here is the list of books in the library: ')
    with open(file_path, 'r') as file_data:
        data_list = file_data.read()
        print(data_list)
        file_data.close()


def updateBook(user_choice, file_path):
    book_id = input('Enter the id of book: ')
    with open(file_path, 'r+') as file_data:
        lines = file_data.readlines()
        book_found = False
        for i, line in enumerate(lines):
            parts = [x.strip() for x in line.strip().split(',')]
            if parts[0] == book_id:
                if user_choice == 3:
                    if parts[3] == 'No':
                        print('Sorry, book is unavailable at the moment. Please revisit next day.')
                        return 0
                    else:
                        parts[3] = 'No'
                        lines[i] = ', '.join(parts)
                        book_found = True
                        break
                else:
                    parts[3] = 'Yes'
                    lines[i] = ', '.join(parts)
                    book_found = True
                    break

        if book_found:
            file_data.seek(0)
            file_data.writelines(lines)
            file_data.truncate()
            if user_choice == 3:
                print(f'Enjoy reading {parts[1]}. Thank you.')
            else:
                print(f'Thank you. {parts[1]} has been returned.')
        else:
            print('Sorry, book not found. Please enter a valid book ID.')
            updateBook(user_choice, file_path)
        file_data.close()


def searchBook(file_path):
    search_input = input('Enter search input: ')
    book_found = False
    with open(file_path, 'r') as file_data:
        for line in file_data:
            if search_input in line:
                print(f'Book found: {line.strip()}')
                book_found = True
                break

        if not book_found:
            print('Sorry, no book found with the given input. Try again!')
            searchBook(file_path)


main()
