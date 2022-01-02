"""
Author:- Sunanda Shil
Date:- 27-12-21
"""
import csv
import logging


logging.basicConfig(filename="address_book.log", filemode="w")


class Contact:
    """
    created class for person address
    """

    def __init__(self, contact_dict):
        """
        created constructor for initialize the variable
        :param contact_dict: this dictionary contain all parameter like firstname,lastname
        """
        self.first_name = contact_dict.get("first_name")
        self.last_name = contact_dict.get("last_name")
        self.age = contact_dict.get("age")
        self.mobile_no = contact_dict.get("mobile_no")
        self.email = contact_dict.get("email")
        self.state = contact_dict.get("state")
        self.pin_no = contact_dict.get("pin_no")

    def set_first_name(self, firstname):
        """
        setter method for firstname
        """
        self.first_name = firstname

    def set_last_name(self, lastname):
        """
        setter method for lastname
        """
        self.last_name = lastname

    def set_ages(self, ages):
        """
        setter method for age
        """
        self.age = ages

    def set_mobile_number(self, mobile_number):
        """
        setter method for mobile number
        """
        self.mobile_no = mobile_number

    def set_email_id(self, email_id):
        """
        setter method for email
        """
        self.email = email_id

    def set_state(self, state_person):
        """
        setter method for state
        """
        self.state = state_person

    def set_pin(self, pin_number):
        """
        setter method for pin number
        """
        self.pin_no = pin_number


class AddressBook:
    """
    created address book class for making require method
    """

    def __init__(self, name):
        self.name = name
        self.contact_list = []

    def add_person(self, person_address):
        """
        Creating this method for adding person in list
        :param person_address: is a object
        """
        self.contact_list.append(person_address)

        with open("address_book.csv", "w") as f:
            for contact in self.contact_list:
                f.write(f"FIRST NAME -> {contact.first_name}\n"
                        f"LAST NAME -> {contact.last_name}\n"
                        f"AGES -> {contact.age}\n"
                        f"STATE -> {contact.state}\n"
                        f"PIN CODE -> {contact.pin_no}\n"
                        f"PHONE NUMBER -> {contact.mobile_no}\n"
                        f"EMAIL -> {contact.email}\n\n")

    def show_details(self):
        """
        for display the inputted value created show details method
        """
        for address in self.contact_list:
            print("The firstname is :-", address.first_name)
            print("The lastname is :- ", address.last_name)
            print("Age of this person is :- ", address.age)
            print("Mobile number is :- ", address.mobile_no)
            print("Email id is :- ", address.email)
            print("The state of this person is :- ", address.state)
            print("Pin number is :- ", address.pin_no)

    def edit_contact(self, contact_names, choices, values):
        """
        For edit the person contact this method has created
        :param contact_names: this name will take from main
        :param choices: choices which user want to edit the contact information
        :param values: user inputted new value which will update in contact
        :return: contact
        """
        for contacts in self.contact_list:
            if contacts.first_name == contact_names:
                contact_dictionary = {1: contacts.set_first_name, 2: contacts.set_last_name, 3: contacts.set_ages,
                                      4: contacts.set_mobile_number, 5: contacts.set_email_id,
                                      6: contacts.set_state, 7: contacts.set_pin}
                contact_dictionary.get(choices)(values)
                return contacts
            else:
                print("Name not found")

    def delete_contact(self, delete_contacts):
        """
        Delete the contact details as per user choice
        """
        try:
            for contacts in self.contact_list:
                if contacts.first_name == delete_contacts:
                    self.contact_list.remove(contacts)
                else:
                    print("Name not found")
        except Exception:
            logging.exception("Type string value!!!")


def get_address_book(multi_address_books, address_books_name):
    """

    :param multi_address_books: for multiple address book
    :param address_books_name: name of the address book
    :return:
    """
    for address_books in multi_address_books:
        if address_book.name == address_books_name:
            return multi_address_books, address_books
    address_books = AddressBook(address_books_name)
    multi_address_books.append(address_books)
    return multi_address_books, address_books


if __name__ == "__main__":
    multi_address_book = []
    try:
        while True:
            print("""
                Choose as per your wish:-
                1.Add person
                2.Show details
                3.Edit details
                4.Delete contact
                5.CSV export
                """)
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                address_book_name = input("Enter the address book name:- ")
                list_of_address_book, address_book = get_address_book(multi_address_book, address_book_name)
                first_name = input("Enter first name:- ")
                last_name = input("Enter last name:- ")
                age = int(input("Enter ages:- "))
                mobile_no = int(input("Enter the mobile number:- "))
                email = input("Enter the email id:- ")
                state = input("Enter the state :-")
                pin_no = int(input("Enter the pin number:- "))

                contact_dict = {"first_name": first_name, "last_name": last_name, "age": age,
                                "mobile_no": mobile_no, "email": email, "state": state, "pin_no": pin_no}
                contact = Contact(contact_dict)
                address_book.add_person(contact)
            elif choice == 2:
                address_book_name = input("Enter the address book name:- ")
                list_of_address_book, address_book = get_address_book(multi_address_book, address_book_name)
                address_book.show_details()
            elif choice == 3:

                address_book_name = input("Enter the address book name:- ")
                list_of_address_book, address_book = get_address_book(multi_address_book, address_book_name)
                try:
                    contact_name = input("Enter the Firstname which you want to edit info:- ")

                    print("""Your choice:-
                           1.First name
                           2.Last name
                           3.Age
                           4.Mobile number
                           5.Email
                           6.State
                           7.Pin number
                           """)
                    choices = int(input("Enter your choice:- "))
                    value = input("Enter the value:- ")
                    address_book.edit_contact(contact_name, choices, value)

                except Exception:
                    logging.exception("Choose proper option!!!")
            elif choice == 4:
                address_book_name = input("Enter the address book name:- ")
                list_of_address_book, address_book = get_address_book(multi_address_book, address_book_name)
                try:
                    delete_contact = input("Enter the first name you want to delete:- ")
                    address_book.delete_contact(delete_contact)
                except Exception:
                    logging.exception("Type proper value!!!")
            elif choice == 5:
                address_book_name = input("Enter the address book name:- ")
                list_of_address_book, address_book = get_address_book(multi_address_book, address_book_name)
                address_book.csv_file()
            else:
                print("Wrong choice!!!")
                break

    except Exception:
        logging.exception("Enter proper value!!!")
